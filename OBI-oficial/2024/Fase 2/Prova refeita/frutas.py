valorReais, numFrutas = map(int, input().split())

tabelaPrecos = {}
quantFrutas = 0

for _ in range(numFrutas):
    if _ >= 100:
        break
    indice, preco = map(int, input().split())
    
    
    if indice not in tabelaPrecos or preco < tabelaPrecos[indice]:
        tabelaPrecos[indice] = preco


sorted_frutas = sorted(tabelaPrecos.items(), key=lambda x: x[1])


for _, preco in sorted_frutas:
    if valorReais < preco:
        break
    valorReais -= preco
    quantFrutas += 1

print(quantFrutas)
