n = int(input())
cadeia = input();

saida = ""

anterior = ""

for i in cadeia:
    if(i == anterior):
        continue

    contagem =  str(cadeia.count(i))
    saida += i + " " + contagem + " "

    while (cadeia.count(i) > 0):
        cadeia = cadeia.replace(i, "")

    anterior = i


print(saida)