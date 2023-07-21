d = int(input('')) #valopr da diaria
a = int(input('')) #aumento da diaria
n = int(input('')) # chegada no hotel

aumenta = 0

mes_falta = 31 - (n-1)

if n > 15:
    n = 15

if n > 1:
    aumenta = n - 1




if n == 1:
    print(31*d)

elif n > 1:
    print(mes_falta * (d + aumenta * a))
