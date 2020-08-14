# 2010 J4

while True:
    line = list(map(int, input().strip().split()))
    if line[0] == 0:
        break
    dif = [line[i + 1] - line[i] for i in range(1, line[0])]
    for i in range(1, line[0]):
        if all(dif[j] == dif[i + j] for j in range(0, line[0] - i - 1)):
            print(i)
            break
    else:
        print(line[0] - 1)

