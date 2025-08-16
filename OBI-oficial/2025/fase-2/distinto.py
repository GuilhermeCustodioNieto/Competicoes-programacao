partidas = int(input())
ultimoMinimo = 0
ultimoMaximo = 0
ultimoValorMaxCaixa = 0
ultimaCaixinha = 0
ultimaParada = 0
ultimoBombom = 0
for j in range(0, partidas):
    

    valorMaxCaixa, minimo, maximo = map(int, input().split())
    
    caixinha = 0
    contagemBombons = 0
    
    ## Otimização zero
    if(ultimoMinimo == minimo & ultimoMaximo == maximo):
        caixinha = ultimaCaixinha

        for i in range(ultimaParada, maximo + 1):
            if(caixinha >= valorMaxCaixa):
                break
            
            contagemBombons += 1
            caixinha += i

        break

    for i in range(minimo, maximo + 1):
        if(caixinha >= valorMaxCaixa):
            break
        
        contagemBombons += 1
        caixinha += i
        ultimaParada = i

    # Otimização zero

    ultimaCaixinha = caixinha
    ultimoBombom = contagemBombons
    ultimoMaximo = maximo
    ultimoMinimo = minimo
    ultimoValorMaxCaixa = valorMaxCaixa

    print(contagemBombons)

# 100, 1, 100