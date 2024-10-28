entrada1 = input()
entrada2 = input()

def verificaSinais(entrada1, entrada2):
    minus1 = len(entrada1) - len(entrada2)
    minus2 = len(entrada2) - len(entrada1)
    
    for i in range(minus1):
        entrada2 = "0" + entrada2
    
    for i in range(minus2):
        entrada1 = "0" + entrada1
    
    return [entrada1, entrada2]

entrada1, entrada2 = map(str, verificaSinais(entrada1, entrada2))

cadeia1 = ""
cadeia2 = ""

for i in range(len(entrada1)):
    intEntrada1 = int(entrada1[i])
    intEntrada2 = int(entrada2[i])
    if(intEntrada1 > intEntrada2):
        cadeia1 += str(intEntrada1)

    elif intEntrada2 > intEntrada1:
        cadeia2 += str(intEntrada2)

    else:
        cadeia1 += str(intEntrada1)
        cadeia2 += str(intEntrada1)

if cadeia1 == '':
    cadeia1 = '-1'

if cadeia2 == '':
    cadeia2 = '-1'

print(cadeia2, cadeia1)
