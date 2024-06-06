# Ordem:
# A própria consoante
# A vogal mais próxima da consoante, e se ela estiver próxima de duas vogais, vai pegar a mais próxima da do inicío do alfabeto
# A consoante mais próxima da origial na ordem do alfabeto

# 1. pegue a consoante uma a uma
# 2. pegue a volgal que está mais próxima da consoante
# 3. pegue a consoante mais próxima a seguir em ordem do alfabeto

# guilherme
# gehuilimhijerosmone

alfabeto = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']

vogais = ['a', 'e', 'i', 'o', 'u']

palavra = input()
novaPalavra = ''

def pegarVogalProxima(consoante):
    # passar de letra em letra
    # pegar o antes e depois da letra
        # ver se alguma é vogal
        #Se nenhuma for vogal, ver as outras duas do antes e depois
    
    # Verificar qual é a mais próxima do alfabeto

    # retornar ao usuário
    posicao = alfabeto.index(consoante)
    quantidadeManutencao = 1
    
    while True:
        antesDaLetra = '' if posicao == 0 else alfabeto[posicao - quantidadeManutencao] # verifica se já estamos no começo da string
        depoisDaLetra = 'z' if alfabeto[posicao] == 'z' or alfabeto[posicao] == 'x' else alfabeto[posicao + quantidadeManutencao] # verifica se já estamos no fim da string

        


        if (antesDaLetra in vogais and depoisDaLetra in vogais) or antesDaLetra in vogais:
            return antesDaLetra
        
        elif depoisDaLetra in vogais:
            return depoisDaLetra

        else:
            quantidadeManutencao += 1

def pegarConsoanteProxima(consoanteOriginal):
    posicaoConsoante = alfabeto.index(consoanteOriginal)
    for letra in alfabeto:
        if posicaoConsoante < alfabeto.index(letra) and (letra not in vogais): # Verifica se a letra atual é a seguir em relação a nossa consoante e também verifica se a letra é consoante
            return letra

    if(posicaoConsoante == alfabeto.index('z')):
        return 'z'

for letra in palavra:
    # pegar a consoante

    consoante = ''

    if(letra not in vogais):
        consoante = letra

        # pegar a vogal mais próxima da palavra
        vogalMaisProxima = pegarVogalProxima(consoante)
        
        # pegar a consoante mais próxima em ordem alfabetica
        proximaConsoante = pegarConsoanteProxima(consoante)

        novaPalavra += consoante
        novaPalavra += vogalMaisProxima
        novaPalavra += proximaConsoante
    else:
        novaPalavra += letra

print(novaPalavra)
