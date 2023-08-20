altura, largura = map(int, input().split())
quantidadeDisp = int(input())

class Moldura:
    def __init__(self, id:int, altura:int, largura:int):
        self.id = id
        self.altura = altura
        self.largura = largura
    
molduras = []


for c in range(quantidadeDisp):
    id = c
    altura = int(input())
    largura = int(input())
    
    mold = Moldura(id, altura, largura)
    
    molduras.append(mold)