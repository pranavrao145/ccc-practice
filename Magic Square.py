import random

num = -7


# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]


def FindSquare():
    while True:
        grid = [[] for i in range(4)]
        for row in grid:
            for element in range(4):
                row.append(int(random.randrange(-30, 30)))
        row1 = grid[0]
        row2 = grid[1]
        row3 = grid[2]
        row4 = grid[3]

        if not row1[0] + row2[0] + row3[0] + row4[0] == num:
            continue
        if not row1[1] + row2[1] + row3[1] + row4[1] == num:
            continue
        if not row1[2] + row2[2] + row3[2] + row4[2] == num:
            continue
        if not row1[3] + row2[3] + row3[3] + row4[3] == num:
            continue
        if not row1[0] + row1[1] + row1[2] + row1[3] == num:
            continue
        if not row2[0] + row2[1] + row2[2] + row2[3] == num:
            continue
        if not row3[0] + row3[1] + row3[2] + row3[3] == num:
            continue
        if not row4[0] + row4[1] + row4[2] + row4[3] == num:
            continue
        if not row1[0] + row2[1] + row3[2] + row4[3] == num:
            continue
        if not row1[3] + row2[2] + row3[1] + row4[0] == num:
            continue
        else:
            return grid


print(FindSquare())
