competidores = []

maior = 0

for c in range(5):
    n = int(input(''))

    competidores.append(n)

maior = competidores[0]
segundo_maior = 0

placas = 0
trofeus = 1

menor = 0

for c in range(1,5):
    if competidores[c] > maior:
        maior = competidores[c]
        trofeus = 1
    elif competidores[c] == maior:
        trofeus += 1

for c in range(1,5):
    if competidores[c] < maior and competidores[c] > segundo_maior:
        segundo_maior = competidores[c]
        placas = 1
    elif competidores[c] < maior and competidores[c] == segundo_maior:
        placas += 1
        

print(trofeus, placas)
#se for digitado fora de ordem de maioridade, vai dar erro