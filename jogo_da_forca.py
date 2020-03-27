import functools
import sys
from time import sleep
from Jogo_da_forca1 import funcoes
from Jogo_da_forca1 import boneco
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QWaitCondition
from Jogo_da_forca1 import design_jogo_da_forca
from Jogo_da_forca1 import design_escolhe_palavra


# class EscolhePalavra(QMainWindow, design_escolhe_palavra.Ui_EscolhePalavra):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         super().setupUi(self)
#         self.setFixedSize(490, 300)
        # self.show()
        # self.okButton.clicked.connect(self.get_text)
        # self.okButton.clicked.connect(self.fecha)
        # self.gettext()

    # def gettext(self):
    #     text, ok = QInputDialog.getText(self, 'Palavra', 'Escolha uma palavra sem que os outros jogadores vejam: ')
    #     if ok:
    #         self.labTesteVariavel.setText(str(text))

    # def get_text(self):
    #     escolha = self.textDigitePalavra.text()
    #     self.labTesteVariavel.setText(escolha)
    #
    # def fecha(self):
    #     if self.textDigitePalavra.text() != '':
    #         self.close()


class JogoDaForca(QMainWindow, design_jogo_da_forca.Ui_JogodaForca):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setFixedSize(790, 600)
        self.erros = 0
        self.palavrastr = 'abcd'.lower().strip().replace(' ', '').replace('-', '')
        self.palavra = funcoes.palavra(self.palavrastr)
        self.digitadas = funcoes.digitadas(self.palavrastr)

        self.show()
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
            # else:
            #     self.labPalavra.setText(funcoes.preencher(self.palavra, self.digitadas, btn.text()))

    def exibe(self):

        self.labPalavra.setText(str(funcoes.exibir(funcoes.digitadas(self.palavra))))
        # self.labPalavra.setText(str(self.palavra))

        self.labErros.setText('Erros = ' + (str(self.erros)))
        self.labForca.setText(str(boneco.forca(self.erros)))

    # def logica_jogo(self, erros, palavrastr, palavra, digitadas):
    #     while True:

            # letra = self.labLetra.text()
            # if letra not in palavrastr and letra in alfabeto:
            #     erros += 1
            #
            # if letra not in alfabeto:
            #     continue
            #
            # funcoes.alfa(letra, alfabeto)
            # funcoes.preencher(palavra, digitadas, letra)
            # if erros == 6:
            #     funcoes.interface(erros, digitadas, alfabeto)
            #     print()
            #     print(f'A palavra era {palavrastr}!')
            #     print('Você perdeu!')
            #     break
            # if funcoes.ganhou(digitadas):
            #     funcoes.interface(erros, digitadas, alfabeto)
            #     print()
            #     print(f'A palavra era {palavrastr}!')
            #     print('Voce ganhou!')
            #     break


# print(palavrastr)
# palavrastr = str(input('Digite uma palavra sem que o jogador veja: '))\
#
#
# palavra = funcoes.palavra(palavrastr)
# digitadas = funcoes.digitadas(palavrastr)
#
# erros = 0

# while True:
#     letra = input('Digite uma letra: ').lower().strip()[0]
#     if letra not in palavrastr and letra in alfabeto:
#         erros += 1
#     if letra not in alfabeto:
#         print('Já foi')
#         continue
#     funcoes.alfa(letra, alfabeto)
#     if len(letra) > 1:
#         print('Digite apenas uma letra')
#         continue
#     funcoes.preencher(palavra, digitadas, letra)
#     if erros == 6:
#         funcoes.interface(erros, digitadas, alfabeto)
#         print()
#         print(f'A palavra era {palavrastr}!')
#         print('Você perdeu!')
#         break
#     if funcoes.ganhou(digitadas):
#         funcoes.interface(erros, digitadas, alfabeto)
#         print()
#         print(f'A palavra era {palavrastr}!')
#         print('Voce ganhou!')
#         break


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    # escolhepalavra = EscolhePalavra()
    jogodaforca = JogoDaForca()
    jogodaforca.show()
    qt.exec_()
