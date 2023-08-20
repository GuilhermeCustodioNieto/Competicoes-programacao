nota1, nota2 = map(float, input('').split())

media = (nota1 + nota2) / 2

if media >= 7:
    print('Aprovado')
elif media >= 4:
    print('Recuperacao')
else:
    print('Reprovado')
