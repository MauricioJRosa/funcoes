## Funções decoradoras potencializam ou modificam a logica de
# outra função ou metodo

# Uma função decoradora é quando utilizamos o @ em cima de uma função

# Exemplo
# @decoradora - decoradora potencializa a função oi com os recursos dela
# def oi():
#  print('oi')

## Criar uma função decoradora

def master(msg):
    def imprime():
        print("esse  e a função decoradora")
    msg()
    return imprime



# criar uma função que vai receber a decoradora

@master
def chama_funcao():
    print("Esta está chamando a função REAL")


## Chamando a função
    
    chama_funcao()
