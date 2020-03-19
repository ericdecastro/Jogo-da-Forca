import sys
from Jogo_da_forca1 import funcoes
from PyQt5.QtWidgets import QApplication,QMainWindow
from Jogo_da_forca1 import design_jogo_da_forca


class JogoDaForca(QMainWindow, design_jogo_da_forca.Ui_JogodaForca):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


        self.btnA.clicked.connect()

funcoes.titulo()
palavrastr = str(input('Digite uma palavra sem que o jogador veja: '))\
    .lower().strip().replace(' ', '').replace('-', '')
palavra = funcoes.palavra(palavrastr)
digitadas = funcoes.digitadas(palavrastr)
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
erros = 0
while True:
    funcoes.interface(erros, digitadas, alfabeto)
    letra = input('Digite uma letra: ').lower().strip()
    if letra not in palavrastr and letra in alfabeto:
        erros += 1
    if letra not in alfabeto:
        print('Já foi')
        continue
    funcoes.alfa(letra, alfabeto)
    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue
    funcoes.preencher(palavra, digitadas, letra)
    if erros == 6:
        funcoes.interface(erros, digitadas, alfabeto)
        print()
        print(f'A palavra era {palavrastr}!')
        print('Você perdeu!')
        break
    if funcoes.ganhou(digitadas):
        funcoes.interface(erros, digitadas, alfabeto)
        print()
        print(f'A palavra era {palavrastr}!')
        print('Voce ganhou!')
        break


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    jogodaforca = JogoDaForca()
    jogodaforca.show()
    qt.exec_()
