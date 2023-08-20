dias_lista = int(input(''))

contadorAcessos, contadorDias, dia_atual = 0


for i in range(dias_lista):
    dia_atual = int(input(''))
    contadorAcessos += dia_atual
    contadorDias += 1

    if contadorAcessos >= 1000000:
        break
    
        

print(contadorDias)
