n = int(input())
lines = []
count = 0
char = " "

for i in range(n):
    lines.append(input())


def Compress(x):
    global count, char
    for i in range(len(x)):
        if i == 0:
            char = x[i]
            count = 1
        elif i != len(x) - 1:
            if x[i] == char:
                count += 1
            else:
                print(count, char, end=" ")
                char = x[i]
                count = 1
        else:
            if x[i] == char:
                count += 1
                print(count, char)
            else:
                print(count, char, end=" ")
                char = x[i]
                count = 1
                print(count, char)


for i in lines:
    Compress(i)