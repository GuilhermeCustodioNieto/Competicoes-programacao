#1. lemos a lista de numeros
#2. vamos percorrer valor por valor da lista e testar todas as suas combinações possiveis
#3. vamos concatenar essa valor com outro DIFERENTE dele
#4. vamos armazenar em um vetor isso
#5 Vamos somar todos os valores do vetor

quantidadeNumeros, numLinhasEntrada = map(str, input().split())

listaNumeros = []
for n in input().split():
    listaNumeros.append(n)

def testaCombinacoes(n, lista):
    concatenaMax = 0
    for i, j in enumerate(lista):
        if(n == i):
            continue

    

        concatena = int(lista[n] + lista[i])
        concatenaMax += concatena
    
    return concatenaMax

entradaPLinhas = []

for x in range(int(numLinhasEntrada)):
    entradaPLinhas.append(input().split())

for x in entradaPLinhas:
    concatenaMax = 0

    for i in range(int(x[0]) - 1, int(x[1])):
        if(x[0] == x[1]):
            continue
        print(listaNumeros[int(x[0]) - 1:int(x[1])])
        print(i)
        concatenaMax += testaCombinacoes(i, listaNumeros[int(x[0]) - 1:int(x[1])])
            
        

    print(concatenaMax)