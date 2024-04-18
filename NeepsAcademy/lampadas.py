# Lampada A e B

# I1 apertado: lampada A acende/apaga
# i2 apertado: inverte A e B trocam de estado juntas.

lampada1 = 0
lampada2 = 0

input()
interruptores = input().split(" ")

def inverte(lampada):
    if lampada == False:
        return 1
    else:
        return 0

for interruptor in interruptores:
    if int(interruptor) == 1:
        lampada1 = inverte(lampada1)

    elif int(interruptor) == 2:
        lampada1 = inverte(lampada1)
        lampada2 = inverte(lampada2)

print(lampada1)
print(lampada2)