n = int(input("Enter a number: "))
flag = 0
counter = 0
y = 0
while True:
    if flag == 0:
        x = int(input("Enter a number that is still in the deck: "))
        y += x
        counter += 1
        if counter == (n - 1):
            flag = 1
    elif flag == 1:
        break
a = n + 1
b = n * a
c = int(b/2)
f = c - y
print(f'The lost card contained {f}.')
