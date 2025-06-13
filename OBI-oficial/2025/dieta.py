quantidadeRefeicoes, limiteCalorias = map(int, input().split())


for i in range(quantidadeRefeicoes):
    proteinas, gorduras, carboidratos = map(int, input().split())
    valorDoDia = (proteinas * 4) + (gorduras * 9) + (carboidratos * 4)
    limiteCalorias -= valorDoDia


print(limiteCalorias)