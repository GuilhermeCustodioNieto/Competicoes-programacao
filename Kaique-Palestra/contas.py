


v = int(input())
a = int(input())
f = int(input())
p = int(input())

menorProMaior = [a, f, p]
menorProMaior.sort()

contador = 0

for i in menorProMaior:
    if(v >= i):
        v -= i
        contador += 1
    else:
        break

print(contador)
