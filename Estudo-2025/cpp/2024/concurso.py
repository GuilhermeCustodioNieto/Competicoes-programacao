tentativas, numMinimo = map(int, input().split())
notas = list(map(int, input().split()))

notas.sort()
print(notas[-numMinimo])