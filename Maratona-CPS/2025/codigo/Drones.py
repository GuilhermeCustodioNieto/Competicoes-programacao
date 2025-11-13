# ler o tamanho de quantos drones tem, se for 0 acaba
# ler as velocidades de cada drone e somar
# ordenar os rankings e pegar o cameão, caso for empate o menor indice vai ser o campeão

tamanho = int(input())
while (tamanho != 0):
    drones = []
    soma = 0
    for i in range(tamanho):
        valores = map(int, input().split())
        for c in valores:
            soma += c
        drones.append([soma, i+1])
        soma = 0
    
    drones.sort(reverse=True)

    print('Drone ' + str(drones[0][1]))

    tamanho = int(input())