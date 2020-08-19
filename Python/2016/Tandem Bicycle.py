# J5

q = int(input())  # question answered
n = int(input())  # citizens from each country
array = []  # stores the speeds of the citizens from each country

for i in range(2):
    f = list(map(int, input().split()))
    array.append(f)


def GetTotalSpeed(x, y):
    bikespeeds = []
    for i in range(len(x)):
        g = (x[i], y[i])
        bikespeeds.append(max(g))
    sum = 0
    for i in bikespeeds:
        sum += i
    return sum


def shift_left_once(lst):
    temp = lst[0]
    i = len(lst) - 1
    for index in range(len(lst) - 1):
        lst[index] = lst[index + 1]
    lst[i] = temp


def GetMinSpeed():
    global n, array
    minspeed = GetTotalSpeed(array[0], array[1])
    for i in range(n):
        shift_left_once(array[0])
        if GetTotalSpeed(array[0], array[1]) < minspeed:
            minspeed = GetTotalSpeed(array[0], array[1])
        else:
            pass
    return minspeed


def GetMaxSpeed():
    global n, array
    maxspeed = GetTotalSpeed(array[0], array[1])
    for i in range(n):
        shift_left_once(array[0])
        if GetTotalSpeed(array[0], array[1]) > maxspeed:
            maxspeed = GetTotalSpeed(array[0], array[1])
        else:
            pass
    return maxspeed


if q == 1:
    print(GetMinSpeed())
else:
    print(GetMaxSpeed())
