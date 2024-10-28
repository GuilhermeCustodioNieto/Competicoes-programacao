import math
num1 = int(input())
num2 = int(input())


contador = 0

def verificaRaiz(num):
    for i in range(10000000):
        if i ** 3 == num and i ** 2 == num:
            print(i)
            return 1
        
    return 0

for i in range(num1, num2 + 1):
    contador += verificaRaiz(i)

print(contador)

