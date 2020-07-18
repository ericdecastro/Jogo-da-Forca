import functools
import sys
import os

from PyQt5.QtMultimedia import QSound, QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import Qt, QRegExp, QRect, QUrl, QFileInfo
from PyQt5.QtGui import QRegExpValidator, QCursor, QFont
from PyQt5.QtWidgets import QPushButton, QDialog
import listadepalavras
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
import design_jogo_da_forca
from random import sample


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


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

font3 = QFont()
font3.setFamily("Century Schoolbook L")
font3.setPointSize(10)
font3.setBold(True)
font3.setWeight(75)


caminhobtndesligado = resource_path('botaodesativado.png')
estilobtndesligado = (f"border-image:url({caminhobtndesligado});\n"
                      "color: rgba(80,45,22,200);")

caminhobtnligado = resource_path('botaoletra.png')
estilobtnligado = (f"border-image:url({caminhobtnligado});\n"
                   "color: rgba(80,45,22,250);")

caminhofundotexto = resource_path('fundotexto.png')
estilofundotexto = (f"border-image: url({caminhofundotexto});"
                    "color: rgba(80,45,22,250);")

caminhobtnmini = resource_path('botaomini.png')
estilobtnmini = f"border-image: url({caminhobtnmini});"

caminhobtnminiapertado = resource_path('botaominiapertado.png')
estilobtnminiapertado = f"border-image: url({caminhobtnminiapertado});"

caminhobtnfechar = resource_path('botaofechar.png')
estilobtnfechar = f"border-image: url({caminhobtnfechar});"

caminhobtnfecharapertado = resource_path('botaofecharapertado.png')
estilobtnfecharapertado = f"border-image: url({caminhobtnfecharapertado});"

caminhosomligado = resource_path('somligado.png')
estilosomligado = f"border-image: url({caminhosomligado});"

caminhosomligadoapertado = resource_path('somligadoapertado.png')
estilosomligadoapertado = f"border-image: url({caminhosomligadoapertado});"

caminhosomdesligado = resource_path('somdesligado.png')
estilosomdesligado = f"border-image: url({caminhosomdesligado});"

caminhosomdesligadoapertado = resource_path('somdesligadoapertado.png')
estilosomdesligadoapertado = f"border-image: url({caminhosomdesligadoapertado});"

caminhofundo1 = resource_path('fundo1.png')

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
    palavrasescolhidas = ''
    categoria = ''

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        self.setWindowTitle('Jogo da Forca')
        self.setGeometry(400, 150, 620, 480)
        self.setFixedSize(660, 570)
        self.setObjectName('palavra')

        self.setStyleSheet(
            f'QWidget#palavra {{border-image: url({caminhofundo1})}}')
        self.caminhointro = resource_path('intro.wav')
        self.intro = QSound(self.caminhointro)
        self.intro.play()

        self.logo = QLabel('', self)
        self.logo.setGeometry(QRect(90, 20, 480, 75))
        self.caminhologo = resource_path("logo.png")
        self.logo.setStyleSheet(
            f"border-image: url({self.caminhologo});"
        )

        self.label1 = QLabel('                Se estiver jogando sozinho escolha uma categoria: ', self)
        self.label1.setFont(font2)
        self.label1.setGeometry(QRect(30, 110, 600, 60))
        self.label1.setStyleSheet(estilofundotexto)

        self.label2 = QLabel('                Se estiver jogando com amigos digite uma palavra\n '
                             '                         sem que os outros jogadores vejam:', self)
        self.label2.setFont(font2)
        self.label2.setGeometry(QRect(30, 340, 600, 80))
        self.label2.setStyleSheet(estilofundotexto)

        self.btnObj = QPushButton('Objetos', self)
        self.btnObj.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnObj.setFont(font)
        self.btnObj.setGeometry(QRect(130, 180, 160, 60))
        self.btnObj.setStyleSheet(estilobtnligado)
        self.btnObj.clicked.connect(functools.partial(self.sorteio, 'Objetos'))
        self.btnObj.clicked.connect(self.hide)
        self.btnObj.pressed.connect(functools.partial(aperta_botao, self.btnObj, 159, 59, estilobtndesligado))
        self.btnObj.released.connect(functools.partial(solta_botao, self.btnObj, 160, 60, estilobtnligado))
        self.btnObj.clicked.connect(functools.partial(clica_botao, self.btnObj, 159, 59, estilobtndesligado))

        self.btnProf = QPushButton('Profissões', self)
        self.btnProf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnProf.setFont(font)
        self.btnProf.setGeometry(QRect(375, 180, 160, 60))
        self.btnProf.setStyleSheet(estilobtnligado)
        self.btnProf.clicked.connect(functools.partial(self.sorteio, 'Profissões'))
        self.btnProf.clicked.connect(self.hide)
        self.btnProf.pressed.connect(functools.partial(aperta_botao, self.btnProf, 159, 59, estilobtndesligado))
        self.btnProf.released.connect(functools.partial(solta_botao, self.btnProf, 160, 60, estilobtnligado))
        self.btnProf.clicked.connect(functools.partial(clica_botao, self.btnProf, 159, 59, estilobtndesligado))

        self.btnPais = QPushButton('Países', self)
        self.btnPais.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPais.setFont(font)
        self.btnPais.setGeometry(QRect(130, 270, 160, 60))
        self.btnPais.setStyleSheet(estilobtnligado)
        self.btnPais.clicked.connect(functools.partial(self.sorteio, 'Países'))
        self.btnPais.clicked.connect(self.hide)
        self.btnPais.pressed.connect(functools.partial(aperta_botao, self.btnPais, 159, 59, estilobtndesligado))
        self.btnPais.released.connect(functools.partial(solta_botao, self.btnPais, 160, 60, estilobtnligado))
        self.btnPais.clicked.connect(functools.partial(clica_botao, self.btnPais, 159, 59, estilobtndesligado))

        self.btnAni = QPushButton('Animais', self)
        self.btnAni.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAni.setFont(font)
        self.btnAni.setGeometry(QRect(375, 270, 160, 60))
        self.btnAni.setStyleSheet(estilobtnligado)
        self.btnAni.clicked.connect(functools.partial(self.sorteio, 'Animais'))
        self.btnAni.clicked.connect(self.hide)
        self.btnAni.pressed.connect(functools.partial(aperta_botao, self.btnAni, 159, 59, estilobtndesligado))
        self.btnAni.released.connect(functools.partial(solta_botao, self.btnAni, 160, 60, estilobtnligado))
        self.btnAni.clicked.connect(functools.partial(clica_botao, self.btnAni, 159, 59, estilobtndesligado))

        self.texto = QLineEdit(self)
        self.texto.setGeometry(QRect(90, 435, 480, 30))
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
        self.btnCancela.setGeometry(QRect(130, 490, 160, 60))
        self.btnCancela.setStyleSheet(estilobtnligado)
        self.btnCancela.clicked.connect(sys.exit)
        self.btnCancela.pressed.connect(functools.partial(aperta_botao, self.btnCancela, 159, 59, estilobtndesligado))
        self.btnCancela.released.connect(functools.partial(solta_botao, self.btnCancela, 160, 60, estilobtnligado))
        self.btnCancela.clicked.connect(functools.partial(clica_botao, self.btnCancela, 159, 59, estilobtndesligado))

        self.btnOk = QPushButton('Confirma', self)
        self.btnOk.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOk.setFont(font)
        self.btnOk.setGeometry(QRect(375, 490, 160, 60))
        self.btnOk.setStyleSheet(estilobtndesligado)
        self.btnOk.clicked.connect(self.hide)
        self.btnOk.clicked.connect(self.usuario)
        self.btnOk.setEnabled(False)
        self.btnOk.pressed.connect(functools.partial(aperta_botao, self.btnOk, 159, 59, estilobtndesligado))
        self.btnOk.released.connect(functools.partial(solta_botao, self.btnOk, 160, 60, estilobtnligado))
        self.btnOk.clicked.connect(functools.partial(clica_botao, self.btnOk, 159, 59, estilobtndesligado))

        self.exec_()

    def usuario(self):
        Palavra.palavrasescolhidas = list(self.texto.text())

    def sorteio(self, categoria):
        if categoria == 'Animais':
            Palavra.palavrasescolhidas = sample(listadepalavras.animais, 3)
            Palavra.categoria = 'Animais'
        if categoria == 'Objetos':
            Palavra.palavrasescolhidas = sample(listadepalavras.objetos, 3)
            Palavra.categoria = 'Objetos'
        if categoria == 'Profissões':
            Palavra.palavrasescolhidas = sample(listadepalavras.profissoes, 3)
            Palavra.categoria = 'Profissões'
        if categoria == 'Países':
            Palavra.palavrasescolhidas = sample(listadepalavras.paises, 3)
            Palavra.categoria = 'Países'

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            pass


class JogoDaForca(QMainWindow, design_jogo_da_forca.Ui_JogodaForca):
    palavra = ''

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setFixedSize(1115, 630)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        self.som = True
        self.erros = 0
        self.caminhoerro = resource_path('errou.wav')
        self.erro = QSound(self.caminhoerro)
        self.caminhoacerto = resource_path('acertou.wav')
        self.acerto = QSound(self.caminhoacerto)
        self.acertos = 0
        self.show()
        self.labPalavra.setText('')
        self.forca()
        self.labCategoria.setText(Palavra.categoria)
        JogoDaForca.palavra = Palavra.palavrasescolhidas

        if len(JogoDaForca.palavra) == 3 and len(JogoDaForca.palavra[1]) > 1:

            self.digitada = [
                self.ver_palavra(0),
                self.ver_palavra(1),
                self.ver_palavra(2)
            ]

            self.labPalavra.setText(''.join(self.digitada[0]))
            self.labPalavra2.setText(''.join(self.digitada[1]))
            self.labPalavra3.setText(''.join(self.digitada[2]))
        else:
            self.labPalavra2.setHidden(True)
            self.labPalavra3.setHidden(True)
            self.labCategoria.setHidden(True)
            self.digitada = [' _ '] * len(JogoDaForca.palavra)
            self.labPalavra.setText(' _ ' * len(JogoDaForca.palavra))
            self.labPalavra.setGeometry(370, 387, 660, 61)
            if len(JogoDaForca.palavra) > 20:
                self.labPalavra.setFont(font3)
                self.labPalavra.setGeometry(370, 387, 660, 61)

        self.forca()

        self.playlist = QMediaPlaylist()
        self.caminhomusica = resource_path('musica.mp3')
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(QFileInfo(self.caminhomusica).absoluteFilePath())))

        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.play()

        self.btnSom.clicked.connect(self.som_liga_desliga)
        self.btnSom.pressed.connect(functools.partial(clica_botao, self.btnSom, 59, 59, estilosomligadoapertado))
        self.btnSom.released.connect(functools.partial(solta_botao, self.btnSom, 60, 60, estilosomligado))

        self.btnFecha.pressed.connect(functools.partial(aperta_botao, self.btnFecha, 40, 40, estilobtnfecharapertado))
        self.btnFecha.released.connect(functools.partial(solta_botao, self.btnFecha, 41, 41, estilobtnfechar))
        self.btnFecha.clicked.connect(sys.exit)

        self.btnMini.pressed.connect(functools.partial(aperta_botao, self.btnMini, 40, 15, estilobtnminiapertado))
        self.btnMini.released.connect(functools.partial(solta_botao, self.btnMini, 41, 16, estilobtnmini))
        self.btnMini.clicked.connect(functools.partial(clica_botao, self.btnMini, 40, 15, estilobtnmini))
        self.btnMini.clicked.connect(self.showMinimized)

        self.btnA.pressed.connect(functools.partial(aperta_botao, self.btnA, 64, 54, estilobtndesligado))
        self.btnA.released.connect(functools.partial(solta_botao, self.btnA, 65, 55, estilobtnligado))
        self.btnA.clicked.connect(functools.partial(clica_botao, self.btnA, 64, 54, estilobtndesligado, letra=True))
        self.btnA.clicked.connect(functools.partial(self.verifica_letra, self.btnA))

        self.btnB.pressed.connect(functools.partial(aperta_botao, self.btnB, 64, 54, estilobtndesligado))
        self.btnB.released.connect(functools.partial(solta_botao, self.btnB, 65, 55, estilobtnligado))
        self.btnB.clicked.connect(functools.partial(clica_botao, self.btnB, 64, 54, estilobtndesligado, letra=True))
        self.btnB.clicked.connect(functools.partial(self.verifica_letra, self.btnB))

        self.btnC.pressed.connect(functools.partial(aperta_botao, self.btnC, 64, 54, estilobtndesligado))
        self.btnC.released.connect(functools.partial(solta_botao, self.btnC, 65, 55, estilobtnligado))
        self.btnC.clicked.connect(functools.partial(clica_botao, self.btnC, 64, 54, estilobtndesligado, letra=True))
        self.btnC.clicked.connect(functools.partial(self.verifica_letra, self.btnC))

        self.btnD.pressed.connect(functools.partial(aperta_botao, self.btnD, 64, 54, estilobtndesligado))
        self.btnD.released.connect(functools.partial(solta_botao, self.btnD, 65, 55, estilobtnligado))
        self.btnD.clicked.connect(functools.partial(clica_botao, self.btnD, 64, 54, estilobtndesligado, letra=True))
        self.btnD.clicked.connect(functools.partial(self.verifica_letra, self.btnD))

        self.btnE.pressed.connect(functools.partial(aperta_botao, self.btnE, 64, 54, estilobtndesligado))
        self.btnE.released.connect(functools.partial(solta_botao, self.btnE, 65, 55, estilobtnligado))
        self.btnE.clicked.connect(functools.partial(clica_botao, self.btnE, 64, 54, estilobtndesligado, letra=True))
        self.btnE.clicked.connect(functools.partial(self.verifica_letra, self.btnE))

        self.btnF.pressed.connect(functools.partial(aperta_botao, self.btnF, 64, 54, estilobtndesligado))
        self.btnF.released.connect(functools.partial(solta_botao, self.btnF, 65, 55, estilobtnligado))
        self.btnF.clicked.connect(functools.partial(clica_botao, self.btnF, 64, 54, estilobtndesligado, letra=True))
        self.btnF.clicked.connect(functools.partial(self.verifica_letra, self.btnF))

        self.btnG.pressed.connect(functools.partial(aperta_botao, self.btnG, 64, 54, estilobtndesligado))
        self.btnG.released.connect(functools.partial(solta_botao, self.btnG, 65, 55, estilobtnligado))
        self.btnG.clicked.connect(functools.partial(clica_botao, self.btnG, 64, 54, estilobtndesligado, letra=True))
        self.btnG.clicked.connect(functools.partial(self.verifica_letra, self.btnG))

        self.btnH.pressed.connect(functools.partial(aperta_botao, self.btnH, 64, 54, estilobtndesligado))
        self.btnH.released.connect(functools.partial(solta_botao, self.btnH, 65, 55, estilobtnligado))
        self.btnH.clicked.connect(functools.partial(clica_botao, self.btnH, 64, 54, estilobtndesligado, letra=True))
        self.btnH.clicked.connect(functools.partial(self.verifica_letra, self.btnH))

        self.btnI.pressed.connect(functools.partial(aperta_botao, self.btnI, 64, 54, estilobtndesligado))
        self.btnI.released.connect(functools.partial(solta_botao, self.btnI, 65, 55, estilobtnligado))
        self.btnI.clicked.connect(functools.partial(clica_botao, self.btnI, 64, 54, estilobtndesligado, letra=True))
        self.btnI.clicked.connect(functools.partial(self.verifica_letra, self.btnI))

        self.btnJ.pressed.connect(functools.partial(aperta_botao, self.btnJ, 64, 54, estilobtndesligado))
        self.btnJ.released.connect(functools.partial(solta_botao, self.btnJ, 65, 55, estilobtnligado))
        self.btnJ.clicked.connect(functools.partial(clica_botao, self.btnJ, 64, 54, estilobtndesligado, letra=True))
        self.btnJ.clicked.connect(functools.partial(self.verifica_letra, self.btnJ))

        self.btnK.pressed.connect(functools.partial(aperta_botao, self.btnK, 64, 54, estilobtndesligado))
        self.btnK.released.connect(functools.partial(solta_botao, self.btnK, 65, 55, estilobtnligado))
        self.btnK.clicked.connect(functools.partial(clica_botao, self.btnK, 64, 54, estilobtndesligado, letra=True))
        self.btnK.clicked.connect(functools.partial(self.verifica_letra, self.btnK))

        self.btnL.pressed.connect(functools.partial(aperta_botao, self.btnL, 64, 54, estilobtndesligado))
        self.btnL.released.connect(functools.partial(solta_botao, self.btnL, 65, 55, estilobtnligado))
        self.btnL.clicked.connect(functools.partial(clica_botao, self.btnL, 64, 54, estilobtndesligado, letra=True))
        self.btnL.clicked.connect(functools.partial(self.verifica_letra, self.btnL))

        self.btnM.pressed.connect(functools.partial(aperta_botao, self.btnM, 64, 54, estilobtndesligado))
        self.btnM.released.connect(functools.partial(solta_botao, self.btnM, 65, 55, estilobtnligado))
        self.btnM.clicked.connect(functools.partial(clica_botao, self.btnM, 64, 54, estilobtndesligado, letra=True))
        self.btnM.clicked.connect(functools.partial(self.verifica_letra, self.btnM))

        self.btnN.pressed.connect(functools.partial(aperta_botao, self.btnN, 64, 54, estilobtndesligado))
        self.btnN.released.connect(functools.partial(solta_botao, self.btnN, 65, 55, estilobtnligado))
        self.btnN.clicked.connect(functools.partial(clica_botao, self.btnN, 64, 54, estilobtndesligado, letra=True))
        self.btnN.clicked.connect(functools.partial(self.verifica_letra, self.btnN))

        self.btnO.pressed.connect(functools.partial(aperta_botao, self.btnO, 64, 54, estilobtndesligado))
        self.btnO.released.connect(functools.partial(solta_botao, self.btnO, 65, 55, estilobtnligado))
        self.btnO.clicked.connect(functools.partial(clica_botao, self.btnO, 64, 54, estilobtndesligado, letra=True))
        self.btnO.clicked.connect(functools.partial(self.verifica_letra, self.btnO))

        self.btnP.pressed.connect(functools.partial(aperta_botao, self.btnP, 64, 54, estilobtndesligado))
        self.btnP.released.connect(functools.partial(solta_botao, self.btnP, 65, 55, estilobtnligado))
        self.btnP.clicked.connect(functools.partial(clica_botao, self.btnP, 64, 54, estilobtndesligado, letra=True))
        self.btnP.clicked.connect(functools.partial(self.verifica_letra, self.btnP))

        self.btnQ.pressed.connect(functools.partial(aperta_botao, self.btnQ, 64, 54, estilobtndesligado))
        self.btnQ.released.connect(functools.partial(solta_botao, self.btnQ, 65, 55, estilobtnligado))
        self.btnQ.clicked.connect(functools.partial(clica_botao, self.btnQ, 64, 54, estilobtndesligado, letra=True))
        self.btnQ.clicked.connect(functools.partial(self.verifica_letra, self.btnQ))

        self.btnR.pressed.connect(functools.partial(aperta_botao, self.btnR, 64, 54, estilobtndesligado))
        self.btnR.released.connect(functools.partial(solta_botao, self.btnR, 65, 55, estilobtnligado))
        self.btnR.clicked.connect(functools.partial(clica_botao, self.btnR, 64, 54, estilobtndesligado, letra=True))
        self.btnR.clicked.connect(functools.partial(self.verifica_letra, self.btnR))

        self.btnS.pressed.connect(functools.partial(aperta_botao, self.btnS, 64, 54, estilobtndesligado))
        self.btnS.released.connect(functools.partial(solta_botao, self.btnS, 65, 55, estilobtnligado))
        self.btnS.clicked.connect(functools.partial(clica_botao, self.btnS, 64, 54, estilobtndesligado, letra=True))
        self.btnS.clicked.connect(functools.partial(self.verifica_letra, self.btnS))

        self.btnT.pressed.connect(functools.partial(aperta_botao, self.btnT, 64, 54, estilobtndesligado))
        self.btnT.released.connect(functools.partial(solta_botao, self.btnT, 65, 55, estilobtnligado))
        self.btnT.clicked.connect(functools.partial(clica_botao, self.btnT, 64, 54, estilobtndesligado, letra=True))
        self.btnT.clicked.connect(functools.partial(self.verifica_letra, self.btnT))

        self.btnU.pressed.connect(functools.partial(aperta_botao, self.btnU, 64, 54, estilobtndesligado))
        self.btnU.released.connect(functools.partial(solta_botao, self.btnU, 65, 55, estilobtnligado))
        self.btnU.clicked.connect(functools.partial(clica_botao, self.btnU, 64, 54, estilobtndesligado, letra=True))
        self.btnU.clicked.connect(functools.partial(self.verifica_letra, self.btnU))

        self.btnV.pressed.connect(functools.partial(aperta_botao, self.btnV, 64, 54, estilobtndesligado))
        self.btnV.released.connect(functools.partial(solta_botao, self.btnV, 65, 55, estilobtnligado))
        self.btnV.clicked.connect(functools.partial(clica_botao, self.btnV, 64, 54, estilobtndesligado, letra=True))
        self.btnV.clicked.connect(functools.partial(self.verifica_letra, self.btnV))

        self.btnW.pressed.connect(functools.partial(aperta_botao, self.btnW, 64, 54, estilobtndesligado))
        self.btnW.released.connect(functools.partial(solta_botao, self.btnW, 65, 55, estilobtnligado))
        self.btnW.clicked.connect(functools.partial(clica_botao, self.btnW, 64, 54, estilobtndesligado, letra=True))
        self.btnW.clicked.connect(functools.partial(self.verifica_letra, self.btnW))

        self.btnX.pressed.connect(functools.partial(aperta_botao, self.btnX, 64, 54, estilobtndesligado))
        self.btnX.released.connect(functools.partial(solta_botao, self.btnX, 65, 55, estilobtnligado))
        self.btnX.clicked.connect(functools.partial(clica_botao, self.btnX, 64, 54, estilobtndesligado, letra=True))
        self.btnX.clicked.connect(functools.partial(self.verifica_letra, self.btnX))

        self.btnY.pressed.connect(functools.partial(aperta_botao, self.btnY, 64, 54, estilobtndesligado))
        self.btnY.released.connect(functools.partial(solta_botao, self.btnY, 65, 55, estilobtnligado))
        self.btnY.clicked.connect(functools.partial(clica_botao, self.btnY, 64, 54, estilobtndesligado, letra=True))
        self.btnY.clicked.connect(functools.partial(self.verifica_letra, self.btnY))

        self.btnZ.pressed.connect(functools.partial(aperta_botao, self.btnZ, 64, 54, estilobtndesligado))
        self.btnZ.released.connect(functools.partial(solta_botao, self.btnZ, 65, 55, estilobtnligado))
        self.btnZ.clicked.connect(functools.partial(clica_botao, self.btnZ, 64, 54, estilobtndesligado, letra=True))
        self.btnZ.clicked.connect(functools.partial(self.verifica_letra, self.btnZ))

    def verifica_letra(self, btn):
        acertou = False
        if len(JogoDaForca.palavra) == 3 and len(JogoDaForca.palavra[1]) > 1:
            for nump, palavra in enumerate(JogoDaForca.palavra):
                for numl, letra in enumerate(palavra):
                    if btn.text().lower() == letra:
                        self.digitada[nump][numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif btn.text().lower() == 'c' and letra in 'ç':
                        self.digitada[nump][numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif btn.text().lower() == 'a' and letra in 'áãâ':
                        self.digitada[nump][numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif btn.text().lower() == 'e' and letra in 'éê':
                        self.digitada[nump][numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif btn.text().lower() == 'i' and letra in 'í':
                        self.digitada[nump][numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif btn.text().lower() == 'o' and letra in 'óõô':
                        self.digitada[nump][numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif btn.text().lower() == 'u' and letra in 'ú':
                        self.digitada[nump][numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif letra != '_':
                        pass
                    else:
                        self.digitada[nump][numl] = ' _ '
        else:

            for numl, letra in enumerate(JogoDaForca.palavra):
                    if btn.text().lower() == letra:
                        self.digitada[numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif btn.text().lower() == 'c' and letra in 'ç':
                        self.digitada[numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif btn.text().lower() == 'a' and letra in 'áãâ':
                        self.digitada[numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif btn.text().lower() == 'e' and letra in 'éê':
                        self.digitada[numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif btn.text().lower() == 'i' and letra in 'í':
                        self.digitada[numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif btn.text().lower() == 'o' and letra in 'óõô':
                        self.digitada[numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif btn.text().lower() == 'u' and letra in 'ú':
                        self.digitada[numl] = f' {letra} '
                        self.acertos += 1
                        acertou = True
                    elif letra != ' _ ':
                        pass
                    else:
                        self.digitada[numl] = ' _ '

        if len(JogoDaForca.palavra) == 3 and len(JogoDaForca.palavra[1]) > 1:
            junta = ''.join(self.digitada[0])
            junta2 = ''.join(self.digitada[1])
            junta3 = ''.join(self.digitada[2])
            self.labPalavra.setText(junta.upper())
            self.labPalavra2.setText(junta2.upper())
            self.labPalavra3.setText(junta3.upper())
        else:
            junta = ''.join(self.digitada)
            self.labPalavra.setText(junta.upper())

        if not acertou:
            self.erros += 1
            if self.som:
                self.erro.play()
        else:
            if self.som:
                self.acerto.play()
        self.forca()
        if len(JogoDaForca.palavra) == 3 and len(JogoDaForca.palavra[1]) > 1:
            if self.acertos == len(JogoDaForca.palavra[0]) + len(JogoDaForca.palavra[1]) + len(JogoDaForca.palavra[2]):
                self.player.stop()
                JogoDaForca.resultado = Resultado()

        else:
            if self.acertos == len(JogoDaForca.palavra):
                self.player.stop()
                JogoDaForca.resultado = Resultado()

        if self.erros >= 6:
            self.player.stop()
            JogoDaForca.resultado = Resultado(ganhou=False)

    def ver_palavra(self, n):
        palavraa = [' _ ']*len(JogoDaForca.palavra[n])
        for num, letra in enumerate(JogoDaForca.palavra[n]):
            if letra == '-':
                palavraa[num] = ' - '
                self.acertos += 1
            elif letra == ' ':
                palavraa[num] = '  '
                self.acertos += 1
            else:
                pass
        return palavraa

    def forca(self):
        self.caminhoforca = resource_path('erro')
        self.labForca.setStyleSheet(
            f"border-image: url({self.caminhoforca+str(self.erros)+'.png'});"
        )

    def som_liga_desliga(self):
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
            f'QWidget#resultado {{ border-image: url({caminhofundo1})}}')

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
            self.caminhoganhou = resource_path('ganhou.wav')
            self.ganhou = QSound(self.caminhoganhou)
            self.ganhou.play()
            self.setGeometry(580, 320, 280, 200)
            self.label = QLabel('          Você ganhou! \n    Quer jogar de novo?', self)
            self.label.setGeometry(QRect(30, 5, 220, 80))
            self.setFixedSize(280, 170)
            self.btnOk.setGeometry(QRect(150, 95, 100, 60))
            self.btnCancela.setGeometry(QRect(30, 95, 100, 60))
        else:
            self.caminhoperdeu = resource_path('perdeu.wav')
            self.perdeu = QSound(self.caminhoperdeu)
            self.perdeu.play()
            if len(JogoDaForca.palavra) == 3 and len(JogoDaForca.palavra[1]) > 1:
                self.label = QLabel(f'    Você perdeu! As palavras eram:\n'
                                    f'    {self.palavra[2].upper()}\n'
                                    f'    {self.palavra[1].upper()}\n'
                                    f'    {self.palavra[0].upper()}\n'
                                    f'    Quer jogar de novo?', self)
                self.setGeometry(550, 280, 380, 190)
                self.label.setGeometry(QRect(30, 0, 340, 180))
                self.setFixedSize(400, 260)
                self.btnOk.setGeometry(QRect(215, 185, 100, 60))
                self.btnCancela.setGeometry(QRect(85, 185, 100, 60))
            else:
                self.palavra = ''.join(self.palavra)
                self.label = QLabel(f'    Você perdeu! A palavra era:\n'
                                    f'    {self.palavra.upper()}\n'
                                    f'    Quer jogar de novo?', self)
                if len(JogoDaForca.palavra) < 19:
                    self.setGeometry(550, 280, 360, 230)
                    self.label.setGeometry(QRect(30, 0, 340, 140))
                    self.setFixedSize(400, 230)
                    self.btnOk.setGeometry(QRect(215, 155, 100, 60))
                    self.btnCancela.setGeometry(QRect(85, 155, 100, 60))
                else:
                    self.setGeometry(450, 280, 550, 230)
                    self.label.setGeometry(QRect(30, 0, 530, 140))
                    self.setFixedSize(590, 230)
                    self.btnOk.setGeometry(QRect(315, 155, 100, 60))
                    self.btnCancela.setGeometry(QRect(175, 155, 100, 60))

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
    palavras = Palavra()
    jogodaforca = JogoDaForca()
    qt.exec_()
