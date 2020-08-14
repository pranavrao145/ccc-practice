# 2010 J3

a = 0
b = 0
flag = 0
nums = '1234567890'

while flag == 0:
    line = input().split()
    for i in range(len(line)):
        if line[i] in nums:
            line[i] = int(line[i])
    if line[0] == 1:
        if line[1] == 'A':
            a = line[2]
        else:
            b = line[2]
    elif line[0] == 2:
        if line[1] == 'A':
            print(a)
        else:
            print(b)
    elif line[0] == 3:
        if line[1] == 'A':
            if line[2] == 'A':
                a = a + a
            else:
                a = a + b
        else:
            if line[2] == 'A':
                b = b + a
            else:
                b = b + b
    elif line[0] == 4:
        if line[1] == 'A':
            if line[2] == 'A':
                a = a * a
            else:
                a = a * b
        else:
            if line[2] == 'A':
                b = b * a
            else:
                b = b * b
    elif line[0] == 5:
        if line[1] == 'A':
            if line[2] == 'A':
                a = a - a
            else:
                a = a - b
        else:
            if line[2] == 'A':
                b = b - a
            else:
                b = b - b
    elif line[0] == 6:
        if line[1] == 'A':
            if line[2] == 'A':
                a = int(a//a)
            else:
                a = int(a//b)
        else:
            if line[2] == 'A':
                b = int(b//a)
            else:
                b = int(b//b)
    else:
        flag = 1