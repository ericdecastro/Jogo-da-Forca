import sys
from Jogo_da_forca1 import funcoes
from Jogo_da_forca1 import boneco
from PyQt5.QtWidgets import QApplication, QMainWindow
from Jogo_da_forca1 import design_jogo_da_forca



alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def let_a():
    print(alfabeto[0])


def let_b():
    print(alfabeto[1])


def let_c():
    print(alfabeto[2])


def let_d():
    print(alfabeto[3])



class JogoDaForca(QMainWindow, design_jogo_da_forca.Ui_JogodaForca):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnA.clicked.connect(let_a)
        self.btnB.clicked.connect(let_b)
        self.btnC.clicked.connect(let_c)


        self.labForca.setText(str(boneco.forca(erros)))
        self.labErros.setText('Erros = ' + (str(erros)))
        self.labAlfabeto.setText(str(funcoes.mostraalfa(alfabeto)))
        self.labPalavra.setText(str(funcoes.exibir(funcoes.digitadas(funcoes.palavra(palavrastr)))))


palavrastr = str(input('Digite uma palavra sem que o jogador veja: '))\
    .lower().strip().replace(' ', '').replace('-', '')
palavra = funcoes.palavra(palavrastr)
digitadas = funcoes.digitadas(palavrastr)

erros = 0

while True:
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
