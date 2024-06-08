numeroLances = int(input())

listaLances = []
lance = []

for i in range(numeroLances):
    nomePessoa = input()
    lancePessoa = int(input())

    lance.append(lancePessoa)
    lance.append(nomePessoa)
    

    listaLances.append(lance)

    lance = []

listaLances.sort()

print(listaLances[-1][1])
print(listaLances[-1][0])