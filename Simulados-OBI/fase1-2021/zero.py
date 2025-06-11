quantidade = int(input())
valores = []
for i in range(0, quantidade):
    valorAdicionado = int(input())
    if valorAdicionado == 0:
        valores.pop()
    else:
        valores.append(valorAdicionado)

print(sum(valores))
