# 2011 J3

coordinates = []
flag = 0
prevcoordinate = [-1, -5]
finaloutput = []


def defaultcoordinates():
    for y in range(-1, -4, -1):
        coordinates.append([0, y])
    for x in range(1, 4):
        coordinates.append([x, -3])
    for y in range(-4, -6, -1):
        coordinates.append([3, y])
    for x in range(4, 6):
        coordinates.append([x, -5])
    for y in range(-4, -2, 1):
        coordinates.append([5, y])
    for x in range(6, 8):
        coordinates.append([x, -3])
    for y in range(-4, -8, -1):
        coordinates.append([7, y])
    for x in range(6, -2, -1):
        coordinates.append([x, -7])
    for y in range(-6, -4, 1):
        coordinates.append([-1, y])


def check(prevcoordinate):
    global coordinates
    if prevcoordinate in coordinates:
        return True
    else:
        return False


def l(x):
    global prevcoordinate, coordinates
    prevcoordinate[0] -= x[1]
    return check(prevcoordinate)


def r(x):
    global prevcoordinate, coordinates
    prevcoordinate[0] += x[1]
    return check(prevcoordinate)


def u(x):
    global prevcoordinate, coordinates
    prevcoordinate[1] += x[1]
    return check(prevcoordinate)


def d(x):
    global prevcoordinate, coordinates
    prevcoordinate[1] -= x[1]
    return check(prevcoordinate)


def safe():
    global prevcoordinate
    print(prevcoordinate[0], prevcoordinate[1], 'safe')
    coordinates.append(prevcoordinate)


def danger():
    global flag
    print(prevcoordinate[0], prevcoordinate[1], 'DANGER')
    flag = 1


defaultcoordinates()
print(coordinates)

while flag == 0:
    x = input().split()
    x[1] = int(x[1])
    if x[0] == 'q':
        flag = 1
    elif x[0] == 'l':
        if not l(x):
            safe()
        else:
            danger()
    elif x[0] == 'r':
        if not r(x):
            safe()
        else:
            danger()
    elif x[0] == 'u':
        if not u(x):
            safe()
        else:
            danger()
    elif x[0] == 'd':
        if not d(x):
            safe()
        else:
            danger()
