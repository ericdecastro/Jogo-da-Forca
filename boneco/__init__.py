def forca(e):
    """
    printa cada fase do desenho de acordo com a quantidade de erros
    :param e: Quantidade de erros do jogador
    :return: retorna cada fase do desenho de acordo com a quantidade de erros
    """
    if e == 0:
        forca_vazia()
    elif e == 1:
        cabeca()
    elif e == 2:
        tronco()
    elif e == 3:
        braco_d()
    elif e == 4:
        braco_e()
    elif e == 5:
        perna_d()
    elif e == 6:
        perna_e()


def forca_vazia():
    print(r"""
_____________
|           |
|           |
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
    print(r"""
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
    print(r"""
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
    print(r"""
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
    print(r"""
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
    print(r"""
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
    print(r"""
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
