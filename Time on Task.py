# 2013 J4

chore_count = 0
max_time = int(input())
chore_times = []
sum_chore_times = 0

for i in range(int(input())):
    chore_times.append(int(input()))

# [5,4,3,2,1]

for i in chore_times:
    if i >= max_time:
        chore_times.remove(i)

# [1,2,3,4,5]

chore_times.sort()

for i in chore_times:
    sum_chore_times += i
    if sum_chore_times <= max_time:
        chore_count += 1


print(chore_count)
