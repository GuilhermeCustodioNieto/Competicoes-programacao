import math

tamanho = int(input())
while (tamanho != 0):
    somaTodosQuilometros = 0
    somaTodosLitros = 0
    melhorConsIndividual = 0
    for i in range(tamanho):
        litros, km = map(int, input().split())
        somaTodosQuilometros += km
        somaTodosLitros += litros
        consumoIndividual = km / litros
        if(consumoIndividual >  melhorConsIndividual):
            melhorConsIndividual = consumoIndividual

    consumoMedioGeral = somaTodosQuilometros / somaTodosLitros
    print(f'Media: {str(consumoMedioGeral).split('.')[0] + '.' + str(consumoMedioGeral).split('.')[1][0]}')
    print(f'Melhor: {str(melhorConsIndividual).split('.')[0] + '.' + str(melhorConsIndividual).split('.')[1][0]}')
    tamanho = int(input())