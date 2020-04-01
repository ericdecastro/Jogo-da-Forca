from Jogo_da_forca1 import boneco


def digitadas(palav):
    digi = []
    for let in palav:
        digi.append('' * len(palav))
    return digi


def exibir(digita):
    """
    Exibe a palavra se formando, ou seja, os espaços da palavra e as letras conforme o jogador vai acertando.
    :param digita: as letras que o jogador digitou e fazem parte da palavra.
    """
    exibida = ''
    for let in digita:
        if let == '':
            exibida += ' _ '
        else:
            exibida += let
    return exibida



def preencher(palav, digi, letra):
    """
    1 - Preenche os espaços da lista 'digitados' quando o jogador acerta uma letra.
    2 - Exclui a letra acertada da lista 'palavra'.
    """
    for n, let in enumerate(palav):
        if let == letra:
            digi[n] = let
            palav[n] = ''


def ganhou(digi):
    acerto = 0
    for let in digi:
        if let != '':
            acerto += 1
    if acerto == len(digi):
        return True
