# Retorna o índice de uma coleção de dados

animais = ["cachorro","Gato","Elefante","Papagaio"]

print(list(enumerate(animais)))

## Iterar uma lista com enumerate 

for i, valor in enumerate(animais):
    print(i,valor)


## Iterador com condicionais

for i, valor in enumerate(animais):
    if i > 1:
        break
    else:
        print(valor)
        

