# Se a bandeja tem mais latas que copos, quebrou
# Se a bandeja tem mais copos,n quebrou

numBandeijas = int(input())

contagemQuebrados = 0

for i in range(numBandeijas):
    latas, copos = input().split(" ")

    latas = int(latas)
    copos = int(copos)

    if latas > copos:
        contagemQuebrados += copos

print(contagemQuebrados)
