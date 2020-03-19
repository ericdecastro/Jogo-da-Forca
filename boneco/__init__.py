def forca(e):
    """
    printa cada fase do desenho de acordo com a quantidade de erros
    :param e: Quantidade de erros do jogador
    :return: retorna cada fase do desenho de acordo com a quantidade de erros
    """
    if e == 0:
        return forca_vazia()
    elif e == 1:
        return cabeca()
    elif e == 2:
        return tronco()
    elif e == 3:
        return braco_d()
    elif e == 4:
        return braco_e()
    elif e == 5:
        return perna_d()
    elif e == 6:
        return perna_e()


def forca_vazia():
    return (r"""
_____________
|                        |
|                        |
|         
|         
|           
|            
|            
|            
|          
|            
|_____________________
|_____________________|        """)


def cabeca():
    return (r"""
_____________
|           |
|          _|_
|         /o o\
|         \_-_/
|           
|            
|            
|            
|          
|            
|_____________________
|_____________________|        """)


def tronco():
    return (r"""
_____________
|           |
|          _|_
|         /o o\
|         \_-_/
|           |
|           | 
|           |  
|            
|          
|            
|_____________________
|_____________________|        """)


def braco_d():
    return (r"""
_____________
|           |
|          _|_
|         /o o\
|         \_-_/
|          _|
|         / | 
|        /  |  
|            
|          
|            
|_____________________
|_____________________|        """)


def braco_e():
    return (r"""
_____________
|           |
|          _|_
|         /o o\
|         \_-_/
|          _|_
|         / | \
|        /  |  \
|            
|          
|            
|_____________________
|_____________________|        """)


def perna_d():
    return (r"""
_____________
|           |
|          _|_
|         /o o\
|         \_-_/
|          _|_
|         / | \
|        /  |  \
|          /   
|        _/   
|            
|_____________________
|_____________________|        """)


def perna_e():
    return (r"""
_____________
|           |
|          _|_
|         /o o\
|         \_-_/
|          _|_
|         / | \
|        /  |  \
|          / \  
|        _/   \_
|            
|_____________________
|_____________________|        """)
