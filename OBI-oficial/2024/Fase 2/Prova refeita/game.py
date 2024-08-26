numInstrucoes = int(input())

instrucoes = input()

resultado = 1

for i in instrucoes:
    if i == 'E':
        resultado = 2 * resultado
    else:
        resultado = 2 * resultado + 1

print(resultado)