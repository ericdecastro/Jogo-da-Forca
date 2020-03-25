import functools
import sys
from Jogo_da_forca1 import funcoes
from Jogo_da_forca1 import boneco
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QInputDialog
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
        erros = 0
        palavrastr = 'abcd'
        palavra = funcoes.palavra(palavrastr)
        digitadas = funcoes.digitadas(palavrastr)
        self.show()
        self.logica_jogo(erros, palavrastr, palavra, digitadas)



        self.btnA.clicked.connect(functools.partial(self.let_botao, 0))
        self.btnB.clicked.connect(functools.partial(self.let_botao, 1))
        self.btnC.clicked.connect(functools.partial(self.let_botao, 2))
        self.btnD.clicked.connect(functools.partial(self.let_botao, 3))
        self.btnE.clicked.connect(functools.partial(self.let_botao, 4))
        self.btnF.clicked.connect(functools.partial(self.let_botao, 5))
        self.btnG.clicked.connect(functools.partial(self.let_botao, 6))
        # self.btnH.clicked.connect(functools.partial(let_botao, 7))
        # self.btnI.clicked.connect(functools.partial(let_botao, 8))
        # self.btnJ.clicked.connect(functools.partial(let_botao, 9))
        # self.btnK.clicked.connect(functools.partial(let_botao, 10))
        # self.btnL.clicked.connect(functools.partial(let_botao, 11))
        # self.btnM.clicked.connect(functools.partial(let_botao, 12))
        # self.btnN.clicked.connect(functools.partial(let_botao, 13))
        # self.btnO.clicked.connect(functools.partial(let_botao, 14))
        # self.btnP.clicked.connect(functools.partial(let_botao, 15))
        # self.btnQ.clicked.connect(functools.partial(let_botao, 16))
        # self.btnR.clicked.connect(functools.partial(let_botao, 17))
        # self.btnS.clicked.connect(functools.partial(let_botao, 18))
        # self.btnT.clicked.connect(functools.partial(let_botao, 19))
        # self.btnU.clicked.connect(functools.partial(let_botao, 20))
        # self.btnV.clicked.connect(functools.partial(let_botao, 21))
        # self.btnW.clicked.connect(functools.partial(let_botao, 22))
        # self.btnX.clicked.connect(functools.partial(let_botao, 23))
        # self.btnY.clicked.connect(functools.partial(let_botao, 24))
        # self.btnZ.clicked.connect(functools.partial(let_botao, 25))


    @staticmethod
    def let_botao(num):
        return alfabeto[num]

    def logica_jogo(self, erros, palavrastr, palavra, digitadas):
        while True:
            self.labAlfabeto.setText(str(funcoes.mostraalfa(alfabeto)))
            self.labPalavra.setText(str(funcoes.exibir(funcoes.digitadas(funcoes.palavra(palavrastr)))))
            self.labErros.setText('Erros = ' + (str(erros)))
            self.labForca.setText(str(boneco.forca(erros)))
            letra = self.let_botao(1)
            if letra not in palavrastr and letra in alfabeto:
                erros += 1

            if letra not in alfabeto:
                continue

            funcoes.alfa(letra, alfabeto)
            funcoes.preencher(palavra, digitadas, letra)
            if erros == 6:
                self.labAlfabeto.setText(str(funcoes.mostraalfa(alfabeto)))
                self.labPalavra.setText(str(funcoes.exibir(funcoes.digitadas(funcoes.palavra(palavrastr)))))
                self.labErros.setText('Erros = ' + (str(erros)))
                self.labForca.setText(str(boneco.forca(erros)))
                funcoes.interface(erros, digitadas, alfabeto)
                print()
                print(f'A palavra era {palavrastr}!')
                print('Você perdeu!')
                break
            if funcoes.ganhou(digitadas):
                self.labAlfabeto.setText(str(funcoes.mostraalfa(alfabeto)))
                self.labPalavra.setText(str(funcoes.exibir(funcoes.digitadas(funcoes.palavra(palavrastr)))))
                self.labErros.setText('Erros = ' + (str(erros)))
                self.labForca.setText(str(boneco.forca(erros)))
                funcoes.interface(erros, digitadas, alfabeto)
                print()
                print(f'A palavra era {palavrastr}!')
                print('Voce ganhou!')
                break


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
