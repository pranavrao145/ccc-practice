# 2018 J3

distances = input().split()

d = []

for i in distances:
    d.append(int(i))

print(0, d[0], d[0] + d[1], d[0] + d[1] + d[2], d[0] + d[1] + d[2] + d[3])
print(d[0], 0, d[1], d[1] + d[2], d[1] + d[2] + d[3])
print(d[0] + d[1], d[1], 0, d[2], d[2] + d[3])
print(d[0] + d[1] + d[2], d[1] + d[2], d[2], 0, d[3])
print(d[0] + d[1] + d[2] + d[3], d[1] + d[2] + d[3], d[2] + d[3], d[3], 0)
