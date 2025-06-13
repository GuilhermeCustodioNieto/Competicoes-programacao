posicaoEscola = int(input())
posicaoSupermercado = int(input())
posicaoLojinha = int(input())

lugares = [posicaoSupermercado, posicaoLojinha]
lugares.sort()

def calcular(num1: int, num2: int):
    if(num1 > num2): return num1 - num2
    else: return num2 - num1

primeiraAndada = calcular(posicaoEscola, lugares[0])
segundaAndada = calcular(lugares[0], lugares[1])
terceiraAndada = calcular(lugares[1], posicaoEscola)

print(primeiraAndada + segundaAndada + terceiraAndada)
