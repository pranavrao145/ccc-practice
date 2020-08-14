n = int(input("Enter a value from 1 to 9:"))
if n <= 9:
    x = ""
    for i in range(1, n + 1):
        i = str(i)
        x = x + i
        print(x)
else:
    print("The program does not accept that input. Please enter a number from 1 to 9.")
