quantidadeEstoqueObjetos, quantidadeTipoObjetos = map(int, input().split())

tabela = list()

listaTipos = []
listaPrecos = []

if(quantidadeEstoqueObjetos != 0):
    listaTipos = list(map(int, input().split()))
    listaPrecos = list(map(int, input().split()))

for i in range(0, quantidadeEstoqueObjetos):
    tabela.append([listaPrecos[i], listaTipos[i]])

# leitura e validação dos clientes 

quantClientes = int(input())
listaClientes = []
if(quantClientes != 0): listaClientes = list(map(int, input().split()))

tabela.sort()

totalLucros = 0

for cliente in listaClientes:
    if cliente == 0:
        totalLucros += tabela[0][0]
        tabela.pop(0)

    else:
        for produto in tabela:
            if(produto[1] == cliente):
                totalLucros += produto[0]
                tabela.remove(produto)
                break

print(totalLucros)