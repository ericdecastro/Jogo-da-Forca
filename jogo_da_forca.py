import functools
import sys
import os

from PyQt5.QtMultimedia import QSound, QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QRegExp, QRect, QUrl
from PyQt5.QtGui import QRegExpValidator, QCursor, QFont
from PyQt5.QtWidgets import QPushButton, QDialog
from Jogo_da_forca1 import boneco
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from Jogo_da_forca1 import design_jogo_da_forca
from random import choice

listapalavras = ['casa', 'bola', 'quarto', 'música', 'abraço', 'viagem', 'violão', 'porta', 'geladeira']

font = QFont()
font.setFamily("Century Schoolbook L")
font.setPointSize(14)
font.setBold(True)
font.setWeight(75)

font2 = QFont()
font2.setFamily("Century Schoolbook L")
font2.setPointSize(13)
font2.setBold(True)
font2.setWeight(75)

estilobtndesligado = ("border-image:url(\"botaodesativado.png\");\n"
                      "color: rgba(80,45,22,200);")

estilobtnligado = ("border-image:url(\"botaoletra.png\");\n"
                   "color: rgba(80,45,22,250);")

estilofundotexto = ("border-image: url(\"fundotexto.png\");"
                    "color: rgba(80,45,22,250);")

estilobtnmini = "border-image: url(\"botaomini.png\");"

estilobtnminiapertado = "border-image: url(\"botaominiapertado.png\");"

estilobtnfechar = "border-image: url(\"botaofechar.png\");"

estilobtnfecharapertado = "border-image: url(\"botaofecharapertado.png\");"

estilosomligado = "border-image: url(\"somligado.png\");"

estilosomligadoapertado = "border-image: url(\"somligadoapertado.png\");"

estilosomdesligado = "border-image: url(\"somdesligado.png\");"

estilosomdesligadoapertado = "border-image: url(\"somdesligadoapertado.png\");"


def aperta_botao(btn, width, height, estilo):
    btn.resize(width, height)
    btn.setStyleSheet(estilo)


def solta_botao(btn, width, height, estilo):
    btn.resize(width, height)
    btn.setStyleSheet(estilo)


def clica_botao(btn, width, height, estilo, letra=False):
    if letra:
        btn.setDisabled(True)
    btn.resize(width, height)
    btn.setStyleSheet(estilo)


class Palavra(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        self.palavraescolhida = ''
        self.setWindowTitle('Palavra')
        self.setGeometry(410, 200, 620, 390)
        self.setFixedSize(620, 390)
        self.setObjectName('palavra')
        self.setStyleSheet(
            'QWidget#palavra { background-image: url("fundomadeira.png")}')

        self.label1 = QLabel('        Se estiver jogando sozinho clique para sortear uma palavra: ', self)
        self.label1.setFont(font2)
        self.label1.setGeometry(QRect(10, 15, 600, 60))
        self.label1.setStyleSheet(estilofundotexto)

        self.label2 = QLabel('                Se estiver jogando com amigos digite uma palavra\n '
                             '                         sem que os outros jogadores vejam:', self)
        self.label2.setFont(font2)
        self.label2.setGeometry(QRect(10, 170, 600, 80))
        self.label2.setStyleSheet(estilofundotexto)

        self.btnSortear = QPushButton('Sortear', self)
        self.btnSortear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSortear.setFont(font)
        self.btnSortear.setGeometry(QRect(240, 90, 140, 60))
        self.btnSortear.setStyleSheet(estilobtnligado)
        self.btnSortear.clicked.connect(self.sorteio)
        self.btnSortear.clicked.connect(self.hide)
        self.btnSortear.pressed.connect(functools.partial(aperta_botao, self.btnSortear, 139, 59, estilobtndesligado))
        self.btnSortear.released.connect(functools.partial(solta_botao, self.btnSortear, 140, 60, estilobtnligado))
        self.btnSortear.clicked.connect(functools.partial(clica_botao, self.btnSortear, 139, 59, estilobtndesligado))

        self.texto = QLineEdit(self)
        self.texto.setGeometry(QRect(70, 260, 480, 30))
        self.texto.setStyleSheet(
            "font-size: 16px;"
        )
        regex = QRegExp(r'[(a-zA-Zà-úÀ-Ú)]{1,29}')
        valida = QRegExpValidator(regex)
        self.texto.setValidator(valida)
        self.texto.textChanged.connect(
            lambda text: self.btnOk.setEnabled(True) if text
            else self.btnOk.setEnabled(False)
        )
        self.texto.textChanged.connect(
            lambda text: self.btnOk.setStyleSheet(estilobtnligado) if text
            else self.btnOk.setStyleSheet(estilobtndesligado)
        )

        self.btnCancela = QPushButton('Sair', self)
        self.btnCancela.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancela.setFont(font)
        self.btnCancela.setGeometry(QRect(170, 310, 140, 60))
        self.btnCancela.setStyleSheet(estilobtnligado)
        self.btnCancela.clicked.connect(sys.exit)
        self.btnCancela.pressed.connect(functools.partial(aperta_botao, self.btnCancela, 139, 59, estilobtndesligado))
        self.btnCancela.released.connect(functools.partial(solta_botao, self.btnCancela, 140, 60, estilobtnligado))
        self.btnCancela.clicked.connect(functools.partial(clica_botao, self.btnCancela, 139, 59, estilobtndesligado))

        self.btnOk = QPushButton('Confirma', self)
        self.btnOk.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOk.setFont(font)
        self.btnOk.setGeometry(QRect(330, 310, 140, 60))
        self.btnOk.setStyleSheet(estilobtndesligado)
        self.btnOk.clicked.connect(self.digitada)
        self.btnOk.clicked.connect(self.hide)
        self.btnOk.setEnabled(False)
        self.btnOk.pressed.connect(functools.partial(aperta_botao, self.btnOk, 139, 59, estilobtndesligado))
        self.btnOk.released.connect(functools.partial(solta_botao, self.btnOk, 140, 60, estilobtnligado))
        self.btnOk.clicked.connect(functools.partial(clica_botao, self.btnOk, 139, 59, estilobtndesligado))

        self.exec_()

    def digitada(self):
        self.palavraescolhida = self.texto.text().lower().strip().replace(' ', '')

    def sorteio(self):
        self.palavraescolhida = choice(listapalavras).lower().strip().replace(' ', '')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            pass


class JogoDaForca(QMainWindow, design_jogo_da_forca.Ui_JogodaForca):
    palavra = ''

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setFixedSize(1045, 625)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        self.som = True
        self.erros = 0
        self.erro = QSound('buzzer.wav')
        # self.acerto = QSound('')
        self.acertos = 0
        self.show()
        self.labPalavra.setText('')
        self.exibe()
        JogoDaForca.palavra = Palavra().palavraescolhida
        if len(JogoDaForca.palavra) > 18:
            self.labPalavra.setStyleSheet(
                f"{estilofundotexto}"
                "font-size: 14px")
        self.digitada = [' _ '] * len(JogoDaForca.palavra)
        self.labPalavra.setText(' _ ' * len(JogoDaForca.palavra))
        self.exibe()

        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(
            QUrl.fromLocalFile('/home/ericdecastro/PycharmProjects/Python_udemy/Jogo_da_forca1/musica.wav')))
        self.player.play()

        self.btnSom.clicked.connect(self.somligadesliga)
        self.btnSom.pressed.connect(functools.partial(clica_botao, self.btnSom, 59, 59, estilosomligadoapertado))
        self.btnSom.released.connect(functools.partial(solta_botao, self.btnSom, 60, 60, estilosomligado))

        self.btnFecha.pressed.connect(functools.partial(aperta_botao, self.btnFecha, 40, 40, estilobtnfecharapertado))
        self.btnFecha.released.connect(functools.partial(solta_botao, self.btnFecha, 41, 41, estilobtnfechar))
        self.btnFecha.clicked.connect(sys.exit)

        self.btnMini.pressed.connect(functools.partial(aperta_botao, self.btnMini, 40, 15, estilobtnminiapertado))
        self.btnMini.released.connect(functools.partial(solta_botao, self.btnMini, 41, 16, estilobtnmini))
        self.btnMini.clicked.connect(functools.partial(clica_botao, self.btnMini, 40, 15, estilobtnmini))
        self.btnMini.clicked.connect(self.showMinimized)

        self.btnA.pressed.connect(functools.partial(aperta_botao, self.btnA, 64, 49, estilobtndesligado))
        self.btnA.released.connect(functools.partial(solta_botao, self.btnA, 65, 50, estilobtnligado))
        self.btnA.clicked.connect(functools.partial(clica_botao, self.btnA, 64, 49, estilobtndesligado, letra=True))
        self.btnA.clicked.connect(functools.partial(self.verifica_letra, self.btnA))

        self.btnB.pressed.connect(functools.partial(aperta_botao, self.btnB, 64, 49, estilobtndesligado))
        self.btnB.released.connect(functools.partial(solta_botao, self.btnB, 65, 50, estilobtnligado))
        self.btnB.clicked.connect(functools.partial(clica_botao, self.btnB, 64, 49, estilobtndesligado, letra=True))
        self.btnB.clicked.connect(functools.partial(self.verifica_letra, self.btnB))

        self.btnC.pressed.connect(functools.partial(aperta_botao, self.btnC, 64, 49, estilobtndesligado))
        self.btnC.released.connect(functools.partial(solta_botao, self.btnC, 65, 50, estilobtnligado))
        self.btnC.clicked.connect(functools.partial(clica_botao, self.btnC, 64, 49, estilobtndesligado, letra=True))
        self.btnC.clicked.connect(functools.partial(self.verifica_letra, self.btnC))

        self.btnD.pressed.connect(functools.partial(aperta_botao, self.btnD, 64, 49, estilobtndesligado))
        self.btnD.released.connect(functools.partial(solta_botao, self.btnD, 65, 50, estilobtnligado))
        self.btnD.clicked.connect(functools.partial(clica_botao, self.btnD, 64, 49, estilobtndesligado, letra=True))
        self.btnD.clicked.connect(functools.partial(self.verifica_letra, self.btnD))

        self.btnE.pressed.connect(functools.partial(aperta_botao, self.btnE, 64, 49, estilobtndesligado))
        self.btnE.released.connect(functools.partial(solta_botao, self.btnE, 65, 50, estilobtnligado))
        self.btnE.clicked.connect(functools.partial(clica_botao, self.btnE, 64, 49, estilobtndesligado, letra=True))
        self.btnE.clicked.connect(functools.partial(self.verifica_letra, self.btnE))

        self.btnF.pressed.connect(functools.partial(aperta_botao, self.btnF, 64, 49, estilobtndesligado))
        self.btnF.released.connect(functools.partial(solta_botao, self.btnF, 65, 50, estilobtnligado))
        self.btnF.clicked.connect(functools.partial(clica_botao, self.btnF, 64, 49, estilobtndesligado, letra=True))
        self.btnF.clicked.connect(functools.partial(self.verifica_letra, self.btnF))

        self.btnG.pressed.connect(functools.partial(aperta_botao, self.btnG, 64, 49, estilobtndesligado))
        self.btnG.released.connect(functools.partial(solta_botao, self.btnG, 65, 50, estilobtnligado))
        self.btnG.clicked.connect(functools.partial(clica_botao, self.btnG, 64, 49, estilobtndesligado, letra=True))
        self.btnG.clicked.connect(functools.partial(self.verifica_letra, self.btnG))

        self.btnH.pressed.connect(functools.partial(aperta_botao, self.btnH, 64, 49, estilobtndesligado))
        self.btnH.released.connect(functools.partial(solta_botao, self.btnH, 65, 50, estilobtnligado))
        self.btnH.clicked.connect(functools.partial(clica_botao, self.btnH, 64, 49, estilobtndesligado, letra=True))
        self.btnH.clicked.connect(functools.partial(self.verifica_letra, self.btnH))

        self.btnI.pressed.connect(functools.partial(aperta_botao, self.btnI, 64, 49, estilobtndesligado))
        self.btnI.released.connect(functools.partial(solta_botao, self.btnI, 65, 50, estilobtnligado))
        self.btnI.clicked.connect(functools.partial(clica_botao, self.btnI, 64, 49, estilobtndesligado, letra=True))
        self.btnI.clicked.connect(functools.partial(self.verifica_letra, self.btnI))

        self.btnJ.pressed.connect(functools.partial(aperta_botao, self.btnJ, 64, 49, estilobtndesligado))
        self.btnJ.released.connect(functools.partial(solta_botao, self.btnJ, 65, 50, estilobtnligado))
        self.btnJ.clicked.connect(functools.partial(clica_botao, self.btnJ, 64, 49, estilobtndesligado, letra=True))
        self.btnJ.clicked.connect(functools.partial(self.verifica_letra, self.btnJ))

        self.btnK.pressed.connect(functools.partial(aperta_botao, self.btnK, 64, 49, estilobtndesligado))
        self.btnK.released.connect(functools.partial(solta_botao, self.btnK, 65, 50, estilobtnligado))
        self.btnK.clicked.connect(functools.partial(clica_botao, self.btnK, 64, 49, estilobtndesligado, letra=True))
        self.btnK.clicked.connect(functools.partial(self.verifica_letra, self.btnK))

        self.btnL.pressed.connect(functools.partial(aperta_botao, self.btnL, 64, 49, estilobtndesligado))
        self.btnL.released.connect(functools.partial(solta_botao, self.btnL, 65, 50, estilobtnligado))
        self.btnL.clicked.connect(functools.partial(clica_botao, self.btnL, 64, 49, estilobtndesligado, letra=True))
        self.btnL.clicked.connect(functools.partial(self.verifica_letra, self.btnL))

        self.btnM.pressed.connect(functools.partial(aperta_botao, self.btnM, 64, 49, estilobtndesligado))
        self.btnM.released.connect(functools.partial(solta_botao, self.btnM, 65, 50, estilobtnligado))
        self.btnM.clicked.connect(functools.partial(clica_botao, self.btnM, 64, 49, estilobtndesligado, letra=True))
        self.btnM.clicked.connect(functools.partial(self.verifica_letra, self.btnM))

        self.btnN.pressed.connect(functools.partial(aperta_botao, self.btnN, 64, 49, estilobtndesligado))
        self.btnN.released.connect(functools.partial(solta_botao, self.btnN, 65, 50, estilobtnligado))
        self.btnN.clicked.connect(functools.partial(clica_botao, self.btnN, 64, 49, estilobtndesligado, letra=True))
        self.btnN.clicked.connect(functools.partial(self.verifica_letra, self.btnN))

        self.btnO.pressed.connect(functools.partial(aperta_botao, self.btnO, 64, 49, estilobtndesligado))
        self.btnO.released.connect(functools.partial(solta_botao, self.btnO, 65, 50, estilobtnligado))
        self.btnO.clicked.connect(functools.partial(clica_botao, self.btnO, 64, 49, estilobtndesligado, letra=True))
        self.btnO.clicked.connect(functools.partial(self.verifica_letra, self.btnO))

        self.btnP.pressed.connect(functools.partial(aperta_botao, self.btnP, 64, 49, estilobtndesligado))
        self.btnP.released.connect(functools.partial(solta_botao, self.btnP, 65, 50, estilobtnligado))
        self.btnP.clicked.connect(functools.partial(clica_botao, self.btnP, 64, 49, estilobtndesligado, letra=True))
        self.btnP.clicked.connect(functools.partial(self.verifica_letra, self.btnP))

        self.btnQ.pressed.connect(functools.partial(aperta_botao, self.btnQ, 64, 49, estilobtndesligado))
        self.btnQ.released.connect(functools.partial(solta_botao, self.btnQ, 65, 50, estilobtnligado))
        self.btnQ.clicked.connect(functools.partial(clica_botao, self.btnQ, 64, 49, estilobtndesligado, letra=True))
        self.btnQ.clicked.connect(functools.partial(self.verifica_letra, self.btnQ))

        self.btnR.pressed.connect(functools.partial(aperta_botao, self.btnR, 64, 49, estilobtndesligado))
        self.btnR.released.connect(functools.partial(solta_botao, self.btnR, 65, 50, estilobtnligado))
        self.btnR.clicked.connect(functools.partial(clica_botao, self.btnR, 64, 49, estilobtndesligado, letra=True))
        self.btnR.clicked.connect(functools.partial(self.verifica_letra, self.btnR))

        self.btnS.pressed.connect(functools.partial(aperta_botao, self.btnS, 64, 49, estilobtndesligado))
        self.btnS.released.connect(functools.partial(solta_botao, self.btnS, 65, 50, estilobtnligado))
        self.btnS.clicked.connect(functools.partial(clica_botao, self.btnS, 64, 49, estilobtndesligado, letra=True))
        self.btnS.clicked.connect(functools.partial(self.verifica_letra, self.btnS))

        self.btnT.pressed.connect(functools.partial(aperta_botao, self.btnT, 64, 49, estilobtndesligado))
        self.btnT.released.connect(functools.partial(solta_botao, self.btnT, 65, 50, estilobtnligado))
        self.btnT.clicked.connect(functools.partial(clica_botao, self.btnT, 64, 49, estilobtndesligado, letra=True))
        self.btnT.clicked.connect(functools.partial(self.verifica_letra, self.btnT))

        self.btnU.pressed.connect(functools.partial(aperta_botao, self.btnU, 64, 49, estilobtndesligado))
        self.btnU.released.connect(functools.partial(solta_botao, self.btnU, 65, 50, estilobtnligado))
        self.btnU.clicked.connect(functools.partial(clica_botao, self.btnU, 64, 49, estilobtndesligado, letra=True))
        self.btnU.clicked.connect(functools.partial(self.verifica_letra, self.btnU))

        self.btnV.pressed.connect(functools.partial(aperta_botao, self.btnV, 64, 49, estilobtndesligado))
        self.btnV.released.connect(functools.partial(solta_botao, self.btnV, 65, 50, estilobtnligado))
        self.btnV.clicked.connect(functools.partial(clica_botao, self.btnV, 64, 49, estilobtndesligado, letra=True))
        self.btnV.clicked.connect(functools.partial(self.verifica_letra, self.btnV))

        self.btnW.pressed.connect(functools.partial(aperta_botao, self.btnW, 64, 49, estilobtndesligado))
        self.btnW.released.connect(functools.partial(solta_botao, self.btnW, 65, 50, estilobtnligado))
        self.btnW.clicked.connect(functools.partial(clica_botao, self.btnW, 64, 49, estilobtndesligado, letra=True))
        self.btnW.clicked.connect(functools.partial(self.verifica_letra, self.btnW))

        self.btnX.pressed.connect(functools.partial(aperta_botao, self.btnX, 64, 49, estilobtndesligado))
        self.btnX.released.connect(functools.partial(solta_botao, self.btnX, 65, 50, estilobtnligado))
        self.btnX.clicked.connect(functools.partial(clica_botao, self.btnX, 64, 49, estilobtndesligado, letra=True))
        self.btnX.clicked.connect(functools.partial(self.verifica_letra, self.btnX))

        self.btnY.pressed.connect(functools.partial(aperta_botao, self.btnY, 64, 49, estilobtndesligado))
        self.btnY.released.connect(functools.partial(solta_botao, self.btnY, 65, 50, estilobtnligado))
        self.btnY.clicked.connect(functools.partial(clica_botao, self.btnY, 64, 49, estilobtndesligado, letra=True))
        self.btnY.clicked.connect(functools.partial(self.verifica_letra, self.btnY))

        self.btnZ.pressed.connect(functools.partial(aperta_botao, self.btnZ, 64, 49, estilobtndesligado))
        self.btnZ.released.connect(functools.partial(solta_botao, self.btnZ, 65, 50, estilobtnligado))
        self.btnZ.clicked.connect(functools.partial(clica_botao, self.btnZ, 64, 49, estilobtndesligado, letra=True))
        self.btnZ.clicked.connect(functools.partial(self.verifica_letra, self.btnZ))

    def verifica_letra(self, btn):
        acertou = False
        for num, letra in enumerate(JogoDaForca.palavra):
            if btn.text().lower() == letra:
                self.digitada[num] = f' {letra} '
                self.acertos += 1
                acertou = True
            elif btn.text().lower() == 'c' and letra in 'ç':
                self.digitada[num] = f' {letra} '
                self.acertos += 1
                acertou = True
            elif btn.text().lower() == 'a' and letra in 'áãâ':
                self.digitada[num] = f' {letra} '
                self.acertos += 1
                acertou = True
            elif btn.text().lower() == 'e' and letra in 'éê':
                self.digitada[num] = f' {letra} '
                self.acertos += 1
                acertou = True
            elif btn.text().lower() == 'i' and letra in 'í':
                self.digitada[num] = f' {letra} '
                self.acertos += 1
                acertou = True
            elif btn.text().lower() == 'o' and letra in 'óõô':
                self.digitada[num] = f' {letra} '
                self.acertos += 1
                acertou = True
            elif btn.text().lower() == 'u' and letra in 'ú':
                self.digitada[num] = f' {letra} '
                self.acertos += 1
                acertou = True
                print(self.acertos)
            elif letra != ' _ ':
                pass
            else:
                self.digitada[num] = ' _ '

        junta = ''.join(self.digitada).upper()
        self.labPalavra.setText(junta)
        if not acertou:
            self.erros += 1
            if self.som:
                self.erro.play()
        self.exibe()

        if self.acertos == len(JogoDaForca.palavra):
            JogoDaForca.resultado = Resultado()
        if self.erros >= 6:
            JogoDaForca.resultado = Resultado(ganhou=False)

    def exibe(self):
        self.labErros.setText('Erros = ' + (str(self.erros)))
        self.labForca.setText(str(boneco.forca(self.erros)))

    def somligadesliga(self):
        if self.som:
            self.btnSom.setStyleSheet(estilosomdesligado)
            self.btnSom.pressed.connect(functools.partial(clica_botao, self.btnSom, 59, 59, estilosomdesligadoapertado))
            self.btnSom.released.connect(functools.partial(solta_botao, self.btnSom, 60, 60, estilosomdesligado))
            self.som = False
            self.player.pause()
        else:
            self.som = True
            self.btnSom.setStyleSheet(estilosomligado)
            self.btnSom.pressed.connect(functools.partial(clica_botao, self.btnSom, 59, 59, estilosomligadoapertado))
            self.btnSom.released.connect(functools.partial(solta_botao, self.btnSom, 60, 60, estilosomligado))
            self.player.play()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            pass


class Resultado(QDialog):
    def __init__(self, parent=None, ganhou=True):
        super().__init__(parent)
        self.setWindowTitle('Jogo da Forca')
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        self.setObjectName('resultado')
        self.setStyleSheet(
            'QWidget#resultado { background-image: url("fundomadeira.png")}')

        self.palavra = JogoDaForca.palavra

        self.btnOk = QPushButton('Sim', self)
        self.btnOk.setFont(font)
        self.btnOk.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOk.setStyleSheet(estilobtnligado)
        self.btnOk.clicked.connect(self.reinicia)
        self.btnOk.pressed.connect(functools.partial(aperta_botao, self.btnOk, 99, 59, estilobtndesligado))
        self.btnOk.released.connect(functools.partial(solta_botao, self.btnOk, 100, 60, estilobtnligado))
        self.btnOk.clicked.connect(functools.partial(clica_botao, self.btnOk, 99, 59, estilobtndesligado))

        self.btnCancela = QPushButton('Não', self)
        self.btnCancela.setFont(font)
        self.btnCancela.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancela.setStyleSheet(estilobtnligado)
        self.btnCancela.clicked.connect(sys.exit)
        self.btnCancela.pressed.connect(functools.partial(aperta_botao, self.btnCancela, 99, 59, estilobtndesligado))
        self.btnCancela.released.connect(functools.partial(solta_botao, self.btnCancela, 100, 60, estilobtnligado))
        self.btnCancela.clicked.connect(functools.partial(clica_botao, self.btnCancela, 99, 59, estilobtndesligado))

        if ganhou:
            self.setGeometry(580, 320, 280, 200)
            self.label = QLabel('          Você ganhou! \n    Quer jogar de novo?', self)
            self.label.setGeometry(QRect(30, 5, 220, 80))
            self.setFixedSize(280, 170)
            self.btnOk.setGeometry(QRect(150, 95, 100, 60))
            self.btnCancela.setGeometry(QRect(30, 95, 100, 60))
        else:
            self.label = QLabel(f'     Voce perdeu! A palavra era:\n     '
                                f'{self.palavra.upper()}\n     Quer jogar de novo?', self)
            if len(self.palavra) > 20:
                self.setGeometry(500, 300, 440, 200)
                self.label.setGeometry(QRect(10, 0, 420, 120))
                self.setFixedSize(440, 200)
                self.btnOk.setGeometry(QRect(240, 130, 100, 60))
                self.btnCancela.setGeometry(QRect(110, 130, 100, 60))
            else:
                self.setGeometry(560, 300, 280, 200)
                self.label.setGeometry(QRect(10, 10, 300, 120))
                self.setFixedSize(320, 210)
                self.btnOk.setGeometry(QRect(170, 135, 100, 60))
                self.btnCancela.setGeometry(QRect(50, 135, 100, 60))

        self.label.setWordWrap(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(estilofundotexto)

        self.exec_()

    @staticmethod
    def reinicia():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            pass


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    jogodaforca = JogoDaForca()
    qt.exec_()
