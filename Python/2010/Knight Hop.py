# J5

class Cell:
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist


def isInside(x, y):
    if 1 <= x <= 8 and 1 <= y <= 8:
        return True
    return False


def MinSteps(originalpos, targetpos):
    dchangex = [2, 2, -2, -2, 1, 1, -1, -1]
    dchangey = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = [Cell(originalpos[0], originalpos[1], 0)]

    visited = [[False for i in range(9)] for j in range(9)]

    while len(queue) > 0:
        t = queue.pop(0)

        if t.x == targetpos[0] and t.y == targetpos[1]:
            return t.dist

        for i in range(8):
            x = t.x + dchangex[i]
            y = t.y + dchangey[i]

            if isInside(x, y) and not visited[x][y]:
                visited[x][y] = True
                queue.append(Cell(x, y, t.dist + 1))


if __name__ == '__main__':
    originalposition = list(map(int, input().split()))
    targetposition = list(map(int, input().split()))
    print(MinSteps(originalposition, targetposition))
