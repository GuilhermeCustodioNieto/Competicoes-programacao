s, t = map(int, input().split())

grafo = [[]]




for i in range(s):
    grafo.append([i+1])

#cada item vai ter seus subItens com cada um dos túneis conectáveis

def verificar(valor1, valor2):
    if grafo[valor1].count(valor2) > 0:
        return True
    else:
        return False

for i in range(t):
    tA, tB = map(int, input().split())
    grafo[tA-1].append(tB)
    grafo[tB-1].append(tA)

T = int(input())
contador = 0

for i in range(T):
    listaViagem = input().split()

    eElegivel = True

    for l in range(len(listaViagem) - 1):
        l = int(l)

        if(l == len(listaViagem) - 1):
            if (verificar(int(listaViagem[l]) - 2, int(listaViagem[l]) - 1) == False):
                eElegivel = False
                print(l)
                print(listaViagem)
        elif(l == 0):
            if (verificar(int(listaViagem[l]) - 1, int(listaViagem[l]) -1 ) == False):
                eElegivel = False
                print(l)
                print(listaViagem)
        else:
            if(verificar(int(listaViagem[l])-1, int(listaViagem[l])) == False):
                eElegivel = False
                print(l)
                print(grafo[l])


    if(eElegivel):
        contador += 1
    
    
    
print(contador)
print(grafo)