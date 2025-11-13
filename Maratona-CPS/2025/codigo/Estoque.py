quantidade = int(input())

while (quantidade != 0):
    estoque = list(map(int, input().split()))
    quantProdutosZero = 0

    tamanho = int(input())
    pedidos = list(map(int, input().split()))
    for pedido in pedidos:
        pedido = pedido - 1
        if(estoque[pedido] == 0):
            continue
        else:
            estoque[pedido] = estoque[pedido] - 1
            
            if(estoque[pedido] == 0):
                quantProdutosZero += 1
    

    print(len(estoque) - quantProdutosZero)
    print(quantProdutosZero)
    quantidade = int(input())