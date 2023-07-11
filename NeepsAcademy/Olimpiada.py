class Pais():
    id = 0
    o = 0
    p = 0
    b = 0

    def aumentaO(self):
        self.o += 1
    
    def aumentaP(self):
        self.p += 1
    
    def aumentaB(self):
        self.b += 1






n, m = map(int, input('').split())

paises = []

maiorO = 0
maiorP = 0
maiorB = 0


for c in range(0, n):
    paises.append(Pais())
    paises[c].id = c+1
    print(c)
    print(paises[c].id)
    print('--')

for c in range(m):
    o, p, b = map(int, input('').split())
    paises[o-1].o += 1
    paises[p-1].p += 1
    paises[b-1].b += 1
    
    print(paises[c].id)
    print(paises[o-1].id)

for c in range(n):
    if 



    print('------------------------------------------')
    print(paises[c].id)
    print(paises[c].o)
    print(paises[c].p)
    print(paises[c].b)

    
