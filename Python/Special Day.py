x = 2
y = 18

a = int(input("Enter a month (1-12): "))
b = int(input("Enter a day (1-31): "))

if a == x:
    if b == y:
        print("SPECIAL")
    elif b > y:
        print("After")
    else:
        print("Before")
elif a < x:
    print("Before")
else:
    print("After")