numeroParticipantes, numMinimoCandidatos = map(int, input().split())

notas = list(map(int, input().split()))

notas.sort()

print(notas[-numMinimoCandidatos])