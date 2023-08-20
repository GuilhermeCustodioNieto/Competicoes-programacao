risada = input('')

vogais = ['a', 'e', 'i', 'o', 'u']

for i in risada:
    if i not in(vogais):
        risada = risada.replace(i, '')

reverso = risada[::-1]



if reverso == risada:
    print('S')
else:
    print('N')