import functools
import sys
import os

from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import Qt, QRegExp, QRect
from PyQt5.QtGui import QRegExpValidator, QCursor, QFont
from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout
from Jogo_da_forca1 import boneco
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog, QDialogButtonBox, \
    QFormLayout, QLabel
from Jogo_da_forca1 import design_jogo_da_forca
from random import choice

listapalavras = ['casa', 'bola', 'quarto', 'música', 'abraço', 'viagem', 'violão', 'porta', 'geladeira']


# class Palavra(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.palavraescolhida = ''
#         self.setWindowTitle('Palavra')
#         self.setGeometry(465, 390, 500, 100)
#         self.setFixedSize(600, 300)
#         # self.setStyleSheet(
#         #     "border-image:url(\"/home/ericdecastro/PycharmProjects/Python_udemy/Jogo_da_forca1/fundomadeira.png\");\n"
#         #     "color: rgba(80,45,22,250);")
#         self.label1 = QLabel('Se estiver jogando sozinho, clique para sortear uma palavra: ', self)
#         self.label2 = QLabel('Se estiver jogando com amigos, digite uma palavra sem que os jogadores vejam: ', self)
#         self.texto = QLineEdit(self)
#         regex = QRegExp(r'[(a-zA-Zà-úÀ-Ú)]+')
#         valida = QRegExpValidator(regex)
#         self.texto.setValidator(valida)
#         self.btnsortear = QPushButton('Sortear', self)
#         self.btnsortear.resize(200,200)
#         # self.btnsortear.setStyleSheet(
#         #     "border-image:url(\"/home/ericdecastro/PycharmProjects/Python_udemy/Jogo_da_forca1/botaoletra.png\");\n"
#         #     "color: rgba(80,45,22,250);")
#         self.btnsortear.clicked.connect(self.sorteio)
#         self.btnsortear.clicked.connect(self.accept)
#         self.btn = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
#         self.btn.button(QDialogButtonBox.Ok).setText("Confirma")
#         self.btn.button(QDialogButtonBox.Cancel).setText("Sair")
#         self.btn.accepted.connect(self.digitada)
#         self.btn.accepted.connect(self.accept)
#         self.btn.rejected.connect(sys.exit)
#         self.btn.button(QDialogButtonBox.Ok).setEnabled(False)
#         self.texto.textChanged.connect(
#             lambda text: self.btn.button(QDialogButtonBox.Ok).setEnabled(True) if text
#             else self.btn.button(QDialogButtonBox.Ok).setEnabled(False)
#         )
#         self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
#         layout = QFormLayout()
#         layout.addWidget(self.label1)
#         layout.addWidget(self.btnsortear)
#         layout.addWidget(self.label2)
#         layout.addWidget(self.texto)
#         layout.addWidget(self.btn)
#         self.setLayout(layout)
#         self.exec_()
#
#     def digitada(self):
#         self.palavraescolhida = self.texto.text().lower().strip().replace(' ', '')
#
#     def sorteio(self):
#         self.palavraescolhida = choice(listapalavras).lower().strip().replace(' ', '')
#
#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key_Escape:
#             pass

class Palavra(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.palavraescolhida = ''
        self.setWindowTitle('Palavra')
        self.setGeometry(465, 390, 500, 100)
        self.setFixedSize(520, 220)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setCentralWidget(self.cw)

        self.font = QFont()
        self.font.setFamily("Century Schoolbook L")
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(75)

        self.label1 = QLabel('Se estiver jogando sozinho, clique para sortear uma palavra: ', self.cw)
        self.label1.setGeometry(QRect(10, 30, 500, 20))

        self.label2 = QLabel('Se estiver jogando com amigos, digite uma palavra sem que os jogadores vejam: ', self.cw)
        self.label2.setGeometry(QRect(10, 80, 500, 20))

        self.texto = QLineEdit(self.cw)
        self.texto.setGeometry(QRect(10, 100, 500, 20))
        regex = QRegExp(r'[(a-zA-Zà-úÀ-Ú)]+')
        valida = QRegExpValidator(regex)
        self.texto.setValidator(valida)

        self.btnSortear = QPushButton('Sortear', self.cw)
        self.btnSortear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSortear.setFont(self.font)
        self.btnSortear.setGeometry(QRect(400, 10, 100, 60))
        self.btnSortear.setStyleSheet(
            "border-image:url(\"/home/ericdecastro/PycharmProjects/Python_udemy/Jogo_da_forca1/botaoletra.png\");\n"
            "color: rgba(80,45,22,250);")
        self.btnSortear.clicked.connect(self.sorteio)
        # self.btnsortear.clicked.connect()

        self.btnOk = QPushButton('Confirma', self.cw)
        self.btnOk.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOk.setFont(self.font)
        self.btnOk.setGeometry(QRect(400, 150, 100, 60))
        self.btnOk.setStyleSheet(
            "border-image:url(\"/home/ericdecastro/PycharmProjects/Python_udemy/Jogo_da_forca1/botaoletra.png\");\n"
            "color: rgba(80,45,22,250);")
        self.btnOk.clicked.connect(self.digitada)
        self.btnOk.setEnabled(False)
        self.texto.textChanged.connect(
            lambda text: self.btnOk.setEnabled(True) if text
            else self.btnOk.setEnabled(False)
        )

        self.btnCancela = QPushButton('Sair', self.cw)
        self.btnCancela.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancela.setFont(self.font)
        self.btnCancela.setGeometry(QRect(290, 150, 100, 60))
        self.btnCancela.setStyleSheet(
            "border-image:url(\"/home/ericdecastro/PycharmProjects/Python_udemy/Jogo_da_forca1/botaoletra.png\");\n"
            "color: rgba(80,45,22,250);")
        self.btnCancela.clicked.connect(sys.exit)

        self.show()

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
        self.setFixedSize(920, 625)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.musica = QSound('musica.wav')
        # self.musica.play()
        self.erros = 0
        self.erro = QSound('buzzer.wav')
        # self.acerto = QSound('')
        self.acertos = 0
        self.show()
        self.labPalavra.setText('')
        self.exibe()
        JogoDaForca.palavra = Palavra().palavraescolhida
        self.digitada = [' _ '] * len(JogoDaForca.palavra)
        self.labPalavra.setText(' _ ' * len(JogoDaForca.palavra))
        self.exibe()
        self.btnFecha.clicked.connect(sys.exit)
        self.btnMini.clicked.connect(self.showMinimized)

        self.btnA.clicked.connect(functools.partial(self.clica_botao, self.btnA))
        self.btnB.clicked.connect(functools.partial(self.clica_botao, self.btnB))
        self.btnC.clicked.connect(functools.partial(self.clica_botao, self.btnC))
        self.btnD.clicked.connect(functools.partial(self.clica_botao, self.btnD))
        self.btnE.clicked.connect(functools.partial(self.clica_botao, self.btnE))
        self.btnF.clicked.connect(functools.partial(self.clica_botao, self.btnF))
        self.btnG.clicked.connect(functools.partial(self.clica_botao, self.btnG))
        self.btnH.clicked.connect(functools.partial(self.clica_botao, self.btnH))
        self.btnI.clicked.connect(functools.partial(self.clica_botao, self.btnI))
        self.btnJ.clicked.connect(functools.partial(self.clica_botao, self.btnJ))
        self.btnK.clicked.connect(functools.partial(self.clica_botao, self.btnK))
        self.btnL.clicked.connect(functools.partial(self.clica_botao, self.btnL))
        self.btnM.clicked.connect(functools.partial(self.clica_botao, self.btnM))
        self.btnN.clicked.connect(functools.partial(self.clica_botao, self.btnN))
        self.btnO.clicked.connect(functools.partial(self.clica_botao, self.btnO))
        self.btnP.clicked.connect(functools.partial(self.clica_botao, self.btnP))
        self.btnQ.clicked.connect(functools.partial(self.clica_botao, self.btnQ))
        self.btnR.clicked.connect(functools.partial(self.clica_botao, self.btnR))
        self.btnS.clicked.connect(functools.partial(self.clica_botao, self.btnS))
        self.btnT.clicked.connect(functools.partial(self.clica_botao, self.btnT))
        self.btnU.clicked.connect(functools.partial(self.clica_botao, self.btnU))
        self.btnV.clicked.connect(functools.partial(self.clica_botao, self.btnV))
        self.btnW.clicked.connect(functools.partial(self.clica_botao, self.btnW))
        self.btnX.clicked.connect(functools.partial(self.clica_botao, self.btnX))
        self.btnY.clicked.connect(functools.partial(self.clica_botao, self.btnY))
        self.btnZ.clicked.connect(functools.partial(self.clica_botao, self.btnZ))


    def clica_botao(self, btn):
        acertou = False
        if btn.clicked:
            btn.setDisabled(True)

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
                elif letra != ' _ ':
                    pass
                else:
                    self.digitada[num] = ' _ '
        junta = ''.join(self.digitada).upper()
        self.labPalavra.setText(junta)
        if not acertou:
            self.erros += 1
            # self.erro.play()
        self.exibe()

        if self.acertos == len(JogoDaForca.palavra):
            Resultado().exec_()
        if self.erros >= 6:
            Resultado(ganhou=False).exec_()

    def exibe(self):
        self.labErros.setText('Erros = ' + (str(self.erros)))
        self.labForca.setText(str(boneco.forca(self.erros)))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            pass


class Resultado(QDialog):
    def __init__(self, parent=None, ganhou=True):
        super().__init__(parent)
        self.setWindowTitle('Jogo da Forca')
        self.setGeometry(600, 400, 500, 100)
        self.palavra = JogoDaForca.palavra
        if ganhou:
            self.setFixedSize(180, 85)
            self.label = QLabel('Você ganhou! \nQuer jogar de novo?')
        else:
            self.setFixedSize((240 + len(self.palavra * 8)), 85)
            self.label = QLabel(f'Voce perdeu! A palavra era: {self.palavra.upper()}\nQuer jogar de novo?')

        self.btn = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.btn.button(QDialogButtonBox.Ok).setText("Sim")
        self.btn.button(QDialogButtonBox.Cancel).setText("Não")
        self.btn.accepted.connect(self.reinicia)
        self.btn.rejected.connect(sys.exit)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        layout = QFormLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        self.setLayout(layout)

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


