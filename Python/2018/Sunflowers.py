# J4

n = int(input())
plantheights = []

for i in range(n):
    x = input().split()
    x = list(map(int, x))
    plantheights.append(x)


def check(table):
    yesno = 0
    for a in range(len(table) - 1):
        for b in range(len(table)):
            if table[a][b] < table[a + 1][b]:
                pass
            else:
                yesno = 1
    for a in range(len(table)):
        for b in range(len(table) - 1):
            if table[a][b] < table[a][b + 1]:
                pass
            else:
                yesno = 1

    if yesno == 1:
        return False
    else:
        return True


def rotate(table):
    global n
    newlist = []
    for i in range(n):
        newlist.append([])
    for a in range(n):
        for b in range(n):
            newlist[a].append(table[b][-(a + 1)])
    return newlist


while not (check(plantheights)):
    plantheights = rotate(plantheights)


for i in plantheights:
    for g in i:
        if i.index(g) != len(i) - 1:
            print(g, end=' ')
        else:
            print(g)
