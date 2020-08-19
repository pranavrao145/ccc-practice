# J4

minutes = int(input())
count = 0
time = 1200

for i in range(minutes):
    time += 1 # 1201
    if time == 1260:
        time = 100
    for a in range(1,12):
        if time == (a*100) + 60:
            time = (a+1) * 100
        else:
            continue
    if len(str(time)) == 3:
        time = str(time)
        x = int(time[0])
        y = int(time[1])
        z = int(time[2])
        if z - y == y - x:
            count += 1
        else:
            pass
    else:
        time = str(time)
        w = int(time[0])
        x = int(time[1])
        y = int(time[2])
        z = int(time[3])
        if z - y == y - x == x - w:
            count += 1
        else:
            pass
    time = int(time)

print(count)