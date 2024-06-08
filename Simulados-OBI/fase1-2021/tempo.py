# 1. ler as falas do chefe e adicionar a uma lista
# 2. para cada 0 na lista, tirar um número
# 3. fazer a soma de todos os números

# etapa 1
quantidadeNumeros = int(input())

numerosLidos = []


for i in range(quantidadeNumeros):
    numerosLidos.append(int(input()))

novaLista = numerosLidos.copy()

# 2. para cada 0 na lista, tirar um número

def tirarZero(posicao):
    novaLista.pop(posicao)
    novaLista.pop(posicao - 1)



for i in range(0, quantidadeNumeros - 1, 1):
    
    if numerosLidos[i] == 0:
        print(i)
        print(novaLista)
        tirarZero(i)
    



# 3. fazer a soma de todos os numeros

