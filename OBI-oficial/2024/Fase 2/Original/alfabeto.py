numAlfabeto, numEntrada = map(int, input().split())

alfabeto = []
for n in input():
    alfabeto.append(n)

entrada = input()

existe = True

for n in entrada:
    if(alfabeto.count(n) == 0):
        existe = False

if(existe):
    print('S')
else:
    print('N')