list1 = []
flag = 0
odd_i = 0

# Generating the list
x = int(input("Enter a number to end the list: "))

while flag == 0:
    y = int(input("Enter a number: "))
    if y == x:
        flag = 1
    list1.append(y)

# find length
n = len(list1) - 1

print(list1)

# find if even or odd
if n % 2 == 0:
    n = n - 1
else:
    n = n - 2

for i in range(n):
    list1[i], list1[i + 1] = list1[i + 1], list1[i]

print(list1)
