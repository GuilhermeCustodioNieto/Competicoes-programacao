dominante = input('')
luanda = [[],[]]
for c in range(3):
    luanda[0].append(input('').upper())

edu = [[],[]]
for c in range(3):
    edu[0].append(input('').upper())

for c in range(3):
    if luanda[0][c][0] == "A":
        luanda[1].append(10)
        


    elif luanda[0][c][0] == "J":
        luanda[1].append(11)
        
    elif luanda[0][c][0] == "Q":
        luanda[1].append(12)
        
    elif luanda[0][c][0] == "K":
        luanda[1].append(13)

    
    if luanda[0][c][1] == dominante[1]:
        luanda[1][-1] += 4 

soma_luanda = 0
for c in range (3):
    soma_luanda += luanda[1][c]

for c in range(3):
    if edu[0][c][0] == "A":
        edu[1].append(10)
        


    elif edu[0][c][0] == "J":
        edu[1].append(11)
        
    elif edu[0][c][0] == "Q":
        edu[1].append(12)
        
    elif edu[0][c][0] == "K":
        edu[1].append(13)

    
    if edu[0][c][1] == dominante[1]:
        edu[1][-1] += 4 

soma_edu = 0
for c in range (3):
    soma_edu += edu[1][c]

if soma_edu > soma_luanda:
    print('Edu')
elif soma_luanda > soma_edu:
    print('Luanda')
else:
    print('empate')