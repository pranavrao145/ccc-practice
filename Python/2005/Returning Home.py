# J3

flag = 0
flag2 = 0
y = ""

directions = []
streets = []

while flag == 0:
    x = input().upper()
    if flag2 % 2 == 1 and x == 'SCHOOL':
        flag = 1
    elif flag2 % 2 == 1:
        streets.append(x)
    elif flag2 % 2 == 0 and (x == 'R' or x == 'L'):
        directions.append(x)
    else:
        print('That is not a valid input.')
        exit()
    flag2 += 1

directions.reverse()
# R, L, R

streets.reverse()
streets.append("HOME")
# JANE, MAIN, HOME

for i in streets:
    r = streets.index(i)
    if i == "HOME":
        if directions[r] == "R":
            y = "LEFT"
        elif directions[r] == "L":
            y = "RIGHT"
        print(f"Turn {y} into {i}.")
    else:
        if directions[r] == "R":
            y = "LEFT"
        elif directions[r] == "L":
            y = "RIGHT"
        print(f"Turn {y} onto {i}.")
