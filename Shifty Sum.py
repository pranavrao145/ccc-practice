n = int(input())
k = int(input())
sum = n

for i in range(1, k + 1):
    sum += n * (10 ** i)

print(sum)
