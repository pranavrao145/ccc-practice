# 2014 J3

n = int(input())

antoniapoints = 100
davidpoints = 100

antoniaroll = 0
davidroll = 0

rolls = []

for i in range(n):
    rolls.append(list(map(int, input().split())))

for i in rolls:
    if i[0] < i[1]:
        antoniapoints -= i[1]
    elif i[1] < i[0]:
        davidpoints -= i[0]
    elif i[0] == i[1]:
        continue

if antoniapoints < 0:
    antoniapoints = 0
if davidpoints < 0:
    davidpoints = 0

print(antoniapoints)
print(davidpoints)