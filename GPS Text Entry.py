# 2008 J3

keyboard = [['A', 'B', 'C', 'D', 'E', 'F'], ['G', 'H', 'I', 'J', 'K', 'L'], ['M', 'N', 'O', 'P', 'Q', 'R'],
            ['S', 'T', 'U', 'V', 'W', 'X'], ['Y', 'Z', ' ', '-', '.', 'enter']]

p = input()
position = [0, 0]
currentposition = [0, 0]
phrase = []
cursormovements = 0
x = 0
y = 0

for i in p:
    phrase.append(i.upper())

for i in phrase: # G P S
    for g in range(5):
        if i in keyboard[g]:
            x = g
            for d in range(6):
                if i in keyboard[g][d]:
                    y = d
    currentposition = [x, y]
    cursormovements += (abs(currentposition[0] - position[0])) + (abs(currentposition[1] - position[1]))
    position = currentposition

currentposition = [4, 5]

cursormovements += (abs(currentposition[0] - position[0])) + (abs(currentposition[1] - position[1]))


print(cursormovements)

