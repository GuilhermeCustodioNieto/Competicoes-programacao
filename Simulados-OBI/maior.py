n = int(input(''))
m = int(input(''))
s = int(input(''))

v_str = ''

lista_total = []
soma = 0

for c in range(n, m+1):
    v_str = str(c)
    # print(v_str)
    for d in range(len(v_str)):
        soma += int(v_str[d])
        # print('sum==', soma)
        # print('v_str == ', v_str[d])
    if soma == s:
        lista_total.append(c)
    
    soma = 0

try:
    maior = max(lista_total)
    print(maior)
except:
    print('-1')