# Receber os valores 
# Fazer uma lista de pessoas infectadas 
# Quando a pessoa infectada tiver contato com uma pessoa não-infectada: adicionar a pessoa não-infectada na lista de infectados
# por fim somar todos os valores do array de infectados

totalDeAmigos, totalReunioes = map(int, input().split())
numAmigoInfectado, primeiraReuniaoInfectado = map(int, input().split())
infectados = set([numAmigoInfectado])
reunioes = []

for _ in range(totalReunioes):
    dados = list(map(int, input().split()))
    participantes = dados[1:]
    reunioes.append(participantes)

for i in range(primeiraReuniaoInfectado - 1, totalReunioes):
    participantes = reunioes[i]

    if any(p in infectados for p in participantes):
        infectados.update(participantes)

print(len(infectados))