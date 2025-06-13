volumeMinimoLeite = int(input())
volumeMaximoLeite = int(input())
capacidadeXicara = int(input())
volumeCafePorDose = int(input())

# multiplicar dores por algum número
# verificar se essa múltiplicação está entre volMin e volMax. Se sim guardar, se menor fazer proxFor, se maior

def validar(iteradorAtual):
    return capacidadeXicara - (volumeCafePorDose * iteradorAtual)

iteradorAtual = 1
while True:
    capacidadeXicaraAtual = validar(iteradorAtual)
    if(capacidadeXicaraAtual >= volumeMinimoLeite and capacidadeXicaraAtual <= volumeMaximoLeite):
        print('S')
        break

    if(capacidadeXicaraAtual > volumeMinimoLeite):
        iteradorAtual += 1
    elif capacidadeXicaraAtual < volumeMaximoLeite:
        print('N') 
        break