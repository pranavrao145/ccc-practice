n = int(input("Enter a number of elements for the list: "))
a = []
counter = 1
for i in range(n):
    a.append(int(input("Enter a number to add to the list: ")))
f = a[0]
for i in range(0,n-1):
    if f != a[i+1]:
        counter += 1
        f = a[i+1]
    else:
        continue
print(counter)