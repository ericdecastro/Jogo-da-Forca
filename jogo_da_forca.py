import functools
import sys
from Jogo_da_forca1 import funcoes
from Jogo_da_forca1 import boneco
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QWaitCondition
from Jogo_da_forca1 import design_jogo_da_forca
from Jogo_da_forca1 import design_escolhe_palavra

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


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


class JogoDaForca(QMainWindow, design_jogo_da_forca.Ui_JogodaForca, ):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setFixedSize(790, 600)
        erros = 0
        palavrastr = 'abcd'
        palavra = funcoes.palavra(palavrastr)
        digitadas = funcoes.digitadas(palavrastr)
        # self.letra = ''
        self.show()
        self.labAlfabeto.setText(str(funcoes.mostraalfa(alfabeto)))
        self.labPalavra.setText(str(funcoes.exibir(funcoes.digitadas(funcoes.palavra(palavrastr)))))
        self.labErros.setText('Erros = ' + (str(erros)))
        self.labForca.setText(str(boneco.forca(erros)))
        # self.logica_jogo(erros, palavrastr, palavra, digitadas)

        self.btnA.clicked.connect(functools.partial(self.click_btn, self.btnA, palavrastr, erros))
        self.btnB.clicked.connect(functools.partial(self.click_btn, self.btnB, palavrastr, erros))
        self.btnC.clicked.connect(functools.partial(self.click_btn, self.btnC, palavrastr, erros))
        self.btnD.clicked.connect(functools.partial(self.click_btn, self.btnD, palavrastr, erros))
        self.btnE.clicked.connect(functools.partial(self.click_btn, self.btnE, palavrastr, erros))
        self.btnF.clicked.connect(functools.partial(self.click_btn, self.btnF, palavrastr, erros))
        self.btnG.clicked.connect(functools.partial(self.click_btn, self.btnG, palavrastr, erros))
        self.btnH.clicked.connect(functools.partial(self.click_btn, self.btnH, palavrastr, erros))
        self.btnI.clicked.connect(functools.partial(self.click_btn, self.btnI, palavrastr, erros))
        self.btnJ.clicked.connect(functools.partial(self.click_btn, self.btnJ, palavrastr, erros))
        self.btnK.clicked.connect(functools.partial(self.click_btn, self.btnK, palavrastr, erros))
        self.btnL.clicked.connect(functools.partial(self.click_btn, self.btnL, palavrastr, erros))
        self.btnM.clicked.connect(functools.partial(self.click_btn, self.btnM, palavrastr, erros))
        self.btnN.clicked.connect(functools.partial(self.click_btn, self.btnN, palavrastr, erros))
        self.btnO.clicked.connect(functools.partial(self.click_btn, self.btnO, palavrastr, erros))
        self.btnP.clicked.connect(functools.partial(self.click_btn, self.btnP, palavrastr, erros))
        self.btnQ.clicked.connect(functools.partial(self.click_btn, self.btnQ, palavrastr, erros))
        self.btnR.clicked.connect(functools.partial(self.click_btn, self.btnR, palavrastr, erros))
        self.btnS.clicked.connect(functools.partial(self.click_btn, self.btnS, palavrastr, erros))
        self.btnT.clicked.connect(functools.partial(self.click_btn, self.btnT, palavrastr, erros))
        self.btnU.clicked.connect(functools.partial(self.click_btn, self.btnU, palavrastr, erros))
        self.btnV.clicked.connect(functools.partial(self.click_btn, self.btnV, palavrastr, erros))
        self.btnW.clicked.connect(functools.partial(self.click_btn, self.btnW, palavrastr, erros))
        self.btnX.clicked.connect(functools.partial(self.click_btn, self.btnX, palavrastr, erros))
        self.btnY.clicked.connect(functools.partial(self.click_btn, self.btnY, palavrastr, erros))
        self.btnZ.clicked.connect(functools.partial(self.click_btn, self.btnZ, palavrastr, erros))

    # def click_btn(self, btn):
    #     self.labLetra.setText(btn.text().lower())
    #     print(btn.text())


    def click_btn(self, btn, palavrastr, erros):
        if btn.clicked:
            if btn.text().lower() not in palavrastr:
                erros += 1
        print(erros)



    @staticmethod
    def let_botao(num):
        return alfabeto[num]

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
#     .lower().strip().replace(' ', '').replace('-', '')
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
