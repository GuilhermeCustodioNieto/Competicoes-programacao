quantidadeQuest = int(input(''))
gabarito = input().upper().strip()
candidato = input().upper().strip()

contagemAcertos = 0

for i in range(quantidadeQuest):
    if candidato[i] == gabarito[i]:
        contagemAcertos += 1

print(contagemAcertos)