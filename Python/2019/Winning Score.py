# J1

Ascores = []
Bscores = []

for i in range(3):
    Ascores.append(int(input()))

Ascore = (Ascores[0]) * 3 + (Ascores[1]) * 2 + (Ascores[2]) * 1

for i in range(3):
    Bscores.append(int(input()))

Bscore = (Bscores[0]) * 3 + (Bscores[1]) * 2 + (Bscores [2]) * 1

if Ascore > Bscore:
    print('A')
elif Ascore == Bscore:
    print('T')
else:
    print('B')


