question = int(input())
n = int(input())

d_speeds = list(map(int, input().strip().split()))
p_speeds = list(map(int, input().strip().split()))

d_speeds.sort()
p_speeds.sort()

total = 0

if question == 2:
    p_speeds = list(reversed(p_speeds))

for i in range(n):
    total += max(d_speeds[i], p_speeds[i])

print(total)