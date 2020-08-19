# J5

found = False
visited = []
matrix = []


def factors(value):
    factors = []
    for i in range(1, value + 1):
        if value % i == 0:
            if i <= down and value / i <= across:
                factors.append((i, int(value / i)))
    return factors


def check(d, a):
    global found, matrix
    if d == down and a == across:
        found = True
        return
    facts = factors(matrix[d - 1][a - 1])
    if not found:
        for elem in facts:
            if elem not in visited:
                visited.append(elem)
                check(elem[0], elem[1])
    return


if __name__ == '__main__':
    down = int(input())
    across = int(input())

    for i in range(down):
        matrix.append(list(map(int, input().strip().split())))

    check(1, 1)

    if found:
        print('yes')
    else:
        print('no')
