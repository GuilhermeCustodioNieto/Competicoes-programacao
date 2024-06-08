valorTotal = int(input())

listaContas = []

listaContas.append(int(input()))
listaContas.append(int(input()))
listaContas.append(int(input()))

contadorContas = 0

listaContas.sort()

for i in listaContas:
    if valorTotal >= i:
        valorTotal -= i
        contadorContas += 1

print(contadorContas)

