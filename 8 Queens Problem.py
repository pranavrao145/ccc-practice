yesno = 0
b = []
for x in range(8):
    user_input = input("Enter a set of coordinates separated by a comma: ")
    b.append([int(i) for i in user_input.split(",")])
print(b)

for i in range(0, 7):
    x = b[i]
    y = b[i + 1]
    if y[0] - x[0] == x[1] - y[1]:
        yesno = 1
        print("These queens can attack each other.")
        exit()
    else:
        for j in range(0, 2):
            if x[j] == y[j]:
                yesno = 1
                print("These queens can attack each other.")
                exit()
            else:
                continue
        continue
if yesno == 0:
    print("These queens cannot attack each other.")
    exit()
