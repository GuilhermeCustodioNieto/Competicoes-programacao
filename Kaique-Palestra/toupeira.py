s, t = map(int, input().split())

grafo = []



for i in range(s):
    grafo.append([i])

#cada item vai ter seus subItens com cada um dos túneis conectáveis

def verificar(valor1, valor2):
    if grafo[valor1].count(valor2) > 0:
        return True
    else:
        return False

for i in (t):
    tA, tB = map(int, input().split())
    grafo[tA-1].append(tB)
    grafo[tB-1].append(tA)

T = int(input())

for i in range(T):
    listaViagem = input().split()
    
