# J4

# Rush hour --> 7(420 mins)-10(600 mins) and  3(900 mins)-7(1140 mins)

hour, minute = list(map(int, input().strip().split(':')))
left = hour * 60 + minute
arrived = left

for minute in range(left, left + 120):
    if arrived >= 420 and arrived < 600 or arrived >= 900 and arrived < 1140:
        arrived += 2
    else:
        arrived += 1

    if arrived == 1400: # 1400 mins make up 24 hrs
        arrived = 0


hours, minutes = 0, 0

while (arrived >= 60):
    arrived -= 60
    hours += 1
    if arrived < 60:
        break

minutes = arrived # whatever is left in arrived (will be < 60)

# formatting

if hours < 10:
    hours = '0' + str(hours)

if minutes < 10:
    minutes = '0' + str(minutes)

print(str(hours) + ":" + str(minutes))