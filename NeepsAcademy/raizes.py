from math import sqrt
import math


quantidadeEntradas = int(input())

allEntradas = map(float, input().split())

soma = 0

for i in allEntradas:
    print(f'{math.sqrt(i):.4f}')