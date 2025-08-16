linhas, colunas = map(int, input().split())

bandeja = []

for i in range(0, linhas):
    leituraLinha = list(map(int, input().split()))
    bandeja.append(leituraLinha)

def verificarAdjascentes(bandeja, linhaValor, colunaValor):
    # acima
    verificado = bandeja[linhaValor - 1][colunaValor]
    soma = verificado + bandeja[linhaValor][colunaValor]
    if(soma % 2 == 0 & verificado != 0):
        pass

    # esquerda

    verificado = bandeja[linhaValor][colunaValor - 1]
    soma = verificado + bandeja[linhaValor][colunaValor]
    if(soma % 2 == 0 & verificado != 0):
        pass

    # direita

    verificado = bandeja[linhaValor][colunaValor + 1]
    soma = verificado + bandeja[linhaValor][colunaValor]
    if(soma % 2 == 0 & verificado != 0):
        pass

    
    # abaixo
    verificado = bandeja[linhaValor + 1][colunaValor]
    soma = verificado + bandeja[linhaValor][colunaValor]
    if(soma % 2 == 0 & verificado != 0):
        pass