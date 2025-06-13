quantidadeBrinquedos = int(input())
quantidadeParticipantesPreferem = list(map(int, input().split()))

# primeiramente eu devo saber o tamanho da matriz pegando o maior valor digitado na lista
# Após isso eu devo criar uma matriz de tamanho maior e len(quantidadeParticipantesPreferem)
# por fim eu devo iterar cada elemento da lista e ir preenchendo coluna por coluna
# agora é só imprimir o gráfico

copiaQuantidadeParticipantes = quantidadeParticipantesPreferem.copy()
copiaQuantidadeParticipantes.sort()

matriz = []
for i in range(copiaQuantidadeParticipantes[-1]):
    matriz.append([])

# iterar a matriz de baixo para cima
# se o primeiro valor da listinha != 0, então a matriz na linha atual (que vai ser da ultima até a primeira) vai ser 1, se não vai ser 0
# subtrair 1 do valor da listinha atual

for i in range(len(matriz) - 1, -1, -1):
    for quantidade in range(len(quantidadeParticipantesPreferem)):
        if(quantidadeParticipantesPreferem[quantidade] != 0):
            matriz[i].append(1)
            quantidadeParticipantesPreferem[quantidade] -= 1
        else:
            matriz[i].append(0)
        

for linha in matriz:
    for coluna in linha:
        print(coluna, end=' ')
    print()