codigo = input('').split()
novaStr = ''
for c in codigo:
    for i in range(1, len(c), 2):
        novaStr += c[i]
    novaStr += " "

print(novaStr)