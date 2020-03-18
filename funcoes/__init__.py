from Jogo_da_forca1 import boneco


def palavra(pstr):
    palav = []
    for n, l in enumerate(pstr):
        palav += pstr[n]
    return palav


def digitadas(palav):
    digi = []
    for let in palav:
        digi.append('' * len(palav))
    return digi


def limpatela():
    import pyautogui
    pyautogui.hotkey('ctrl', 'l')


def exibir(digita):
    """
    Exibe a palavra se formando, ou seja, os espaços da palavra e as letras conforme o jogador vai acertando.
    :param digita: as letras que o jogador digitou e fazem parte da palavra.
    """
    print(end='                           ')
    for let in digita:
        if let == '':
            print(' _ ', end='')
        else:
            print(let, end='')
    print()


def preencher(palav, digi, letra):
    """
    1 - Preenche os espaços da lista 'digitados' quando o jogador acerta uma letra.
    2 - Exclui a letra acertada da lista 'palavra'.
    """
    for n, let in enumerate(palav):
        if let == letra:
            digi[n] = let
            palav[n] = ''


def alfa(l, alfab):
    """
    Remove as letras digitadas da lista 'alfabeto'.
    :param l: letra digitada pelo usuário.
    :param alfab: Recebe a lista 'alfabeto'
    """
    if l in alfab:
        for n, let in enumerate(alfab):
            if let == l:
                alfab[n] = '_'


def mostraalfa(alfab):
    """
    Exibe o alfabeto com exceção das letras que ja foram digitadas.
    """
    for let in alfab:
        print(let, end=' ')
    print()


def ganhou(digi):
    acerto = 0
    for let in digi:
        if let != '':
            acerto += 1
    if acerto == len(digi):
        return True


def titulo():
    print()
    print('-' * 40)
    print(f'{"JOGO DA FORCA":^40}')
    print('-' * 40)
    print()


def interface(err, dig, alfab):
    limpatela()
    titulo()
    print(f'erros = {err}')
    boneco.forca(err)
    exibir(dig)
    print()
    mostraalfa(alfab)
    print()
