telefonePrimario = input('')

teclas = [[],['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I'],['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], [ 'W', 'X', 'Y', 'Z']]


telefoneNovo = ''

for c in telefonePrimario:
    for i, z in enumerate(teclas):
        for x in z:
            if c == x:
                telefonePrimario = telefonePrimario.replace(x, str(i+1))
print(telefonePrimario)

