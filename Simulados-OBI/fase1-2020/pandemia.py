# Receber os valores 
# Fazer uma lista de pessoas infectadas 
# Quando a pessoa infectada tiver contato com uma pessoa não-infectada: adicionar a pessoa não-infectada na lista de infectados
# por fim somar todos os valores do array de infectados

totalDeAmigos, totalReunioes = map(int, input().split())
numAmigoInfectado, primeiraReuniaoInfectado = map(int, input().split())
reunioes = []


for i in range(0, totalReunioes):
    reunioes.append(list(map(int, input().split())))
    reunioes[-1].pop(0)

infectados = [numAmigoInfectado]
def merge(array1, array2):
    finalArray = []
    for i in array1:
        if i not in finalArray: finalArray.append(i)
    for i in array2:
        if i not in finalArray: finalArray.append(i)
    return finalArray

for i in range(primeiraReuniaoInfectado - 1, totalReunioes):
    participantesDaReuniao = reunioes[i]
    
    for p in participantesDaReuniao:
        if p in infectados:
            infectados = merge(infectados, participantesDaReuniao)



print(len(infectados))
    
    