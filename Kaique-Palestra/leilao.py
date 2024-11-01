n = int(input())

maior = 0
nomeMaior = 0

for i in range(n):
    nome = input()
    lance = int(input())

    if lance > maior:
        maior = lance
        nomeMaior = nome

print(nomeMaior)
print(maior)