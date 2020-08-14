# 2019 J4

row1 = [1, 2]
row2 = [3, 4]


def HorizontalFlip():
    global row1, row2
    row1[0], row2[0] = row2[0], row1[0]
    row1[1], row2[1] = row2[1], row1[1]


def VerticalFlip():
    global row1, row2
    row1[0], row1[1] = row1[1], row1[0]
    row2[0], row2[1] = row2[1], row2[0]


for i in (input()).upper():
    if i == "H":
        HorizontalFlip()
    elif i == "V":
        VerticalFlip()

print(row1[0], row1[1])
print(row2[0], row2[1])
