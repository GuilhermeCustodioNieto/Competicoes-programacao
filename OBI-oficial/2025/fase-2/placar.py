totalGols = set()
momentosGolsPaulo = set()
momentosGolsCamila = set()

# leitura do Paulo

entradasPaulo = list(map(int, input().split()))

golsPaulo = entradasPaulo[0]

for i in range(1, golsPaulo + 1):
    totalGols.add(entradasPaulo[i])
    momentosGolsPaulo.add(entradasPaulo[i])

# leitura da camila

entradasCamila = list(map(int, input().split()))

golsCamila = entradasCamila[0]

for i in range(1, golsCamila + 1):
    totalGols.add(entradasCamila[i])
    momentosGolsCamila.add(entradasCamila[i])

contagemGolsPaulo = 0
contagemGolsCamila = 0

print('0 0')

totalGols = list(totalGols)
totalGols.sort()
for i in totalGols:
    if(momentosGolsPaulo.__contains__(i)):
        contagemGolsPaulo += 1
    else:
        contagemGolsCamila += 1

    print('' + str(contagemGolsPaulo) + ' ' + str(contagemGolsCamila))