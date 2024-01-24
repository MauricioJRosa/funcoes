# A função MAP tem como objetivo aplicar um função ou ação em todos os elementos de uma estrutura 
# de dados retornando uma nova sequencia ou resultado


import math

lista = [1,5,3,15,78]

def soma(x):
    return x+2

print(tuple(map(soma,lista)))

print(list(map(math.sqrt,lista)))