## Função Filter filtra elementos de uma estrutura de dados e filtra o valor que queremos encontrar


listamista = [1,"João","Pedro",53]

def busca(x):
    return x == "João"

# Forma Não otimizada
print(list(filter(busca,listamista)))

# Forma Otimizada
print(list(filter(lambda x: x == "Pedro",listamista)))