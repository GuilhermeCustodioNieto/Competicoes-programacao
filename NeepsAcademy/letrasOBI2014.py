letra = input('')
texto = input('')

novoTexto = texto.split()

contador = 0

for i in novoTexto:
    if i.count(letra) > 0:
        contador += 1

calculo = (contador*100)/len(novoTexto)

print(f'{calculo:.1f}')