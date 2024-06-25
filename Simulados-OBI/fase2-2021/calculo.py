numS = int(input())
numInicio = int(input())
numFim = int(input())
    
contador = 0




for i in range(numInicio, numFim + 1):

    
    unidades = []
    for n in str(i):
        unidades.append(int(n))
    

    if sum(unidades) == numS:
            contador += 1


print(contador)

