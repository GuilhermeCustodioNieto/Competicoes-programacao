p1, c1, p2, c2 = map(int, input().split())

esquerdo = p1 * c1
direito = p2 * c2

if (esquerdo) == (direito):
    print(0)
elif esquerdo > direito:
    print(-1)
else: 
    print(1)