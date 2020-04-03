import functools
import sys
import os

from PyQt5.QtCore import Qt


from Jogo_da_forca1 import boneco
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QDialog, QDialogButtonBox, \
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

            if self.erros == 6:
                self.resultado(ganhou=False)
            if self.acertos == len(self.palavra):
                self.resultado()

    def exibe(self):
        self.labErros.setText('Erros = ' + (str(self.erros)))
        self.labForca.setText(str(boneco.forca(self.erros)))

    def resultado(self, ganhou=True):
        boxr = QMessageBox()
        boxr.setWindowTitle('Jogo da Forca')
        boxr.setGeometry(600, 400, 500, 100)
        boxr.setFixedSize(280, 100)
        if ganhou:
            boxr.setText('Voce ganhou! Quer jogar de novo?')
        else:
            boxr.setText(f'Voce perdeu! A palavra era: {self.palavra.upper()}\nQuer jogar de novo?')
        boxr.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        btn_s = boxr.button(QMessageBox.Yes)
        btn_s.setText('Sim')
        btn_n = boxr.button(QMessageBox.No)
        btn_n.setText('Não')
        boxr.exec_()

        if boxr.clickedButton() == btn_s:
            self.reinicia()
        if boxr.clickedButton() == btn_n:
            sys.exit()

    def funcao_palavra(self):

        boxp = QDialog()
        boxp.setWindowTitle('Palavra')
        boxp.setGeometry(560, 400, 500, 100)
        boxp.setFixedSize(330, 100)
        boxp.label = QLabel('Digite uma palavra sem que os jogadores vejam: ', boxp)
        boxp.texto = QLineEdit(boxp)
        boxp.btn = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        boxp.btn.accepted.connect(boxp.accept)
        boxp.btn.rejected.connect(self.fechar)
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

        return boxp.texto.text().lower().strip().replace(' ', '').replace('-', '')

    @staticmethod
    def fechar():
        sys.exit()

    @staticmethod
    def reinicia():
        python = sys.executable
        os.execl(python, python, *sys.argv)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    jogodaforca = JogoDaForca()
    qt.exec_()


