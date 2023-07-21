# n = int(input(''))
# cadeia = input('')

sub_cadeia = []
cadeia = 'vovossorirmirim'

def palindromo(p = ''):
    p=p.replace(' ', '')

    reverse = []
    lista = []
    palindromo2 = ''

    for c, i in enumerate(p):
        reverse.append(i)

    for c in range(len(lista)):
        lista.append(p)    

    for c in range(1, len(p)+1):
        palindromo2 += p[-c]
        
    if p == palindromo2:
        return True
    else:
        return False

n = 15
n2 = n*2//2

for i in range(n2):
    for c in range(n2):
        sub_cadeia.append(cadeia[i:c])

n = sub_cadeia.count('')

final = []
final2 = []
contador = 0

for c in range(n):
    sub_cadeia.remove('')

for i,c in enumerate(sub_cadeia):
    if palindromo(c) == True:
        if final.count(c) == 1:
            pass
        else:
            final.append(c)
            contador +=1
            print(final)


print(contador)



        