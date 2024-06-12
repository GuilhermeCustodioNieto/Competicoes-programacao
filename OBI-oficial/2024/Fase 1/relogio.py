horas = int(input())
minutos = int(input())
segundos = int(input())

segundosAdiado = int(input())

# Convert all time to seconds
total_segundos = horas * 3600 + minutos * 60 + segundos
# Add the specified seconds
total_segundos += segundosAdiado

# Calculate the new time components
horas = (total_segundos // 3600) % 24
minutos = (total_segundos // 60) % 60
segundos = total_segundos % 60

print(horas)
print(minutos)
print(segundos)
