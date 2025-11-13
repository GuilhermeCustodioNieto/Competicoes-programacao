tamanho = int(input())
while (tamanho != 0):
    pessoasNoElevador = 0
    maiorQuantidadePessoas = 0
    for i in range(tamanho):
        entrando, saindo = map(int, input().split())
        pessoasNoElevador += entrando
        pessoasNoElevador -= saindo
        if(pessoasNoElevador > maiorQuantidadePessoas):
            maiorQuantidadePessoas = pessoasNoElevador
    print(maiorQuantidadePessoas)

    tamanho = int(input())