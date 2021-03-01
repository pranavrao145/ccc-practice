M = int(input())
N = int(input())

choices = int(input())

row = [0] * M
column = [0] * N

for i in range(choices):
    rc, num = input().split()

    num = int(num) - 1

    if rc == 'R':
        row[num] = 1 if row[num] == 0 else 0
    else:
        column[num] = 1 if column[num] == 0 else 0

ans = 0

col_sum = sum([1 - e for e in column])
row_sum = sum([1 - e for e in row])

for elem in row:
    ans += elem * col_sum

for elem in column:
    ans += elem * row_sum

print(ans)
