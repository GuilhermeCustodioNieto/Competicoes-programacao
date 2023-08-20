quantidade = int(input(''))

lista = [0,0,0,0,0,0,0,0,0,0]

for i in range(quantidade):
    atual = int(input(''))
    for c in str(atual):
        for x in range(10):
            if c == str(x):
                lista[x] += 1
        
for i, c in enumerate(lista):
    print(f'{i} - {c}')