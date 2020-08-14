flag = 0
namesandfunctions = {}
n = int(input("Enter the number of files: "))

for i in range(1, n + 1):
    x = input("Enter the name of the file: ")
    y = input("Enter the functions applicable for this file (separated by a comma): ").split(",")
    namesandfunctions[x] = y


def checkflag(u):
    if u == 0:
        print("OK")
    else:
        print("Access Denied")


print("FILE REQUESTS")
p = int(input("Enter the amount of files to request: "))
for j in range(1, p + 1):
    z = input("Enter the filename: ")
    a = input("Enter the file requests: ").split(",")
    for i in a:
        if i in namesandfunctions.get(z):
            flag = 0
            continue
        else:
            flag = 1
            checkflag(flag)
