import functools
import sys
import os

from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator


from Jogo_da_forca1 import boneco
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog, QDialogButtonBox, \
    QFormLayout, QLabel
from Jogo_da_forca1 import design_jogo_da_forca


class JogoDaForca(QMainWindow, design_jogo_da_forca.Ui_JogodaForca, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.palavra = ''
        self.setFixedSize(840, 540)
        self.erros = 0
        self.acertos = 0
        self.show()
        self.labPalavra.setText('')
        self.exibe()
        self.palavra = self.funcao_palavra()
        self.digitada = [' _ '] * len(self.palavra)
        self.labPalavra.setText(' _ ' * len(self.palavra))
        self.exibe()

        self.btnA.clicked.connect(functools.partial(self.click_btn, self.btnA))
        self.btnB.clicked.connect(functools.partial(self.click_btn, self.btnB))
        self.btnC.clicked.connect(functools.partial(self.click_btn, self.btnC))
        self.btnD.clicked.connect(functools.partial(self.click_btn, self.btnD))
        self.btnE.clicked.connect(functools.partial(self.click_btn, self.btnE))
        self.btnF.clicked.connect(functools.partial(self.click_btn, self.btnF))
        self.btnG.clicked.connect(functools.partial(self.click_btn, self.btnG))
        self.btnH.clicked.connect(functools.partial(self.click_btn, self.btnH))
        self.btnI.clicked.connect(functools.partial(self.click_btn, self.btnI))
        self.btnJ.clicked.connect(functools.partial(self.click_btn, self.btnJ))
        self.btnK.clicked.connect(functools.partial(self.click_btn, self.btnK))
        self.btnL.clicked.connect(functools.partial(self.click_btn, self.btnL))
        self.btnM.clicked.connect(functools.partial(self.click_btn, self.btnM))
        self.btnN.clicked.connect(functools.partial(self.click_btn, self.btnN))
        self.btnO.clicked.connect(functools.partial(self.click_btn, self.btnO))
        self.btnP.clicked.connect(functools.partial(self.click_btn, self.btnP))
        self.btnQ.clicked.connect(functools.partial(self.click_btn, self.btnQ))
        self.btnR.clicked.connect(functools.partial(self.click_btn, self.btnR))
        self.btnS.clicked.connect(functools.partial(self.click_btn, self.btnS))
        self.btnT.clicked.connect(functools.partial(self.click_btn, self.btnT))
        self.btnU.clicked.connect(functools.partial(self.click_btn, self.btnU))
        self.btnV.clicked.connect(functools.partial(self.click_btn, self.btnV))
        self.btnW.clicked.connect(functools.partial(self.click_btn, self.btnW))
        self.btnX.clicked.connect(functools.partial(self.click_btn, self.btnX))
        self.btnY.clicked.connect(functools.partial(self.click_btn, self.btnY))
        self.btnZ.clicked.connect(functools.partial(self.click_btn, self.btnZ))

    def click_btn(self, btn):
        if btn.clicked:
            btn.setDisabled(True)
            if btn.text().lower() not in self.palavra:
                self.erros += 1
                self.exibe()

            else:
                for num, letra in enumerate(self.palavra):

                    if btn.text().lower() == letra:
                        self.digitada[num] = f' {letra} '
                        self.acertos += 1
                    elif letra != ' _ ':
                        pass
                    else:
                        self.digitada[num] = ' _ '
            junta = ''.join(self.digitada).upper()
            self.labPalavra.setText(junta)
            self.exibe()

            if self.erros >= 6:
                self.resultado(ganhou=False)
            if self.acertos == len(self.palavra):
                self.resultado()

    def exibe(self):
        self.labErros.setText('Erros = ' + (str(self.erros)))
        self.labForca.setText(str(boneco.forca(self.erros)))

    def resultado(self, ganhou=True):
        boxr = QDialog()
        boxr.setWindowTitle('Jogo da Forca')
        boxr.setGeometry(600, 400, 500, 100)
        boxr.setFixedSize((240 + len(self.palavra*8)), 85)

        if ganhou:
            boxr.label = QLabel('Você ganhou! \nQuer jogar de novo?')
        else:
            boxr.label = QLabel(f'Voce perdeu! A palavra era: {self.palavra.upper()}\nQuer jogar de novo?')
        boxr.btn = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        boxr.btn.button(QDialogButtonBox.Ok).setText("Sim")
        boxr.btn.button(QDialogButtonBox.Cancel).setText("Não")
        boxr.btn.accepted.connect(self.reinicia)
        boxr.btn.rejected.connect(sys.exit)

        boxr.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        layout = QFormLayout()
        layout.addWidget(boxr.label)
        layout.addWidget(boxr.btn)
        boxr.setLayout(layout)
        boxr.exec_()

    def funcao_palavra(self):
        boxp = QDialog()
        boxp.setWindowTitle('Palavra')
        boxp.setGeometry(560, 400, 500, 100)
        boxp.setFixedSize(330, 100)
        boxp.label = QLabel('Digite uma palavra sem que os jogadores vejam: ', boxp)
        boxp.texto = QLineEdit(boxp)
        regex = QRegExp(r'[(a-zA-Zà-úÀ-Ú)]+')
        valida = QRegExpValidator(regex)
        boxp.texto.setValidator(valida)
        boxp.btn = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        boxp.btn.button(QDialogButtonBox.Ok).setText("Confirma")
        boxp.btn.button(QDialogButtonBox.Cancel).setText("Cancelar")
        boxp.btn.accepted.connect(boxp.accept)
        boxp.btn.rejected.connect(sys.exit)
        boxp.btn.button(QDialogButtonBox.Ok).setEnabled(False)
        boxp.texto.textChanged.connect(
            lambda text: boxp.btn.button(QDialogButtonBox.Ok).setEnabled(True) if text
            else boxp.btn.button(QDialogButtonBox.Ok).setEnabled(False)
        )
        boxp.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        layout = QFormLayout()
        layout.addWidget(boxp.label)
        layout.addWidget(boxp.texto)
        layout.addWidget(boxp.btn)
        boxp.setLayout(layout)
        boxp.exec_()
        return boxp.texto.text().lower().strip().replace(' ', '')

    @staticmethod
    def reinicia():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Escape:
    #         sys.exit()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    jogodaforca = JogoDaForca()
    qt.exec_()


