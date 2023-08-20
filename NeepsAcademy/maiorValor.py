num1 = int(input(''))
num2 = int(input(''))
num3 = int(input(''))

maior = 0

value = 0

soma = 0
for i in range(num1, num2):
    for c in range(num1, i):
        soma += c
        if soma > maior:
            maior = i

    
        

print(maior)