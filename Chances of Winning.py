# 2013 J5
# TODO: Fix bugs

from itertools import product
from copy import copy

favteam = int(input())
gamesdone = int(input())
points = [0 for i in range(4)]
played = []
notplayed = []
counter = 0


def UpdatePoints():
    for i in range(gamesdone):
        line = list(map(int, input().strip().split()))
        teama = line[0]
        teamb = line[1]
        teamascore = line[2]
        teambscore = line[3]
        if teamascore > teambscore:
            points[teama - 1] += 3
        elif teambscore > teamascore:
            points[teamb - 1] += 3
        else:
            points[teama - 1] += 1
            points[teamb - 1] += 1
        played.append((teama, teamb))


def NotPlayed():
    for i in range(1, 5):
        for j in range(1, 5):
            if i == j:
                continue
            else:
                if (i, j) not in played and (j, i) not in played:
                    notplayed.append((i, j))
                    played.append((i, j))


def GenerateOutcomes():
    outcomes = []
    for i in notplayed:
        outcomes.append([i[0], i[1], f'{i[0]}T{i[1]}'])
        return CalculateOutcomes(outcomes)


def CalculateOutcomes(outcomes):
    return list(product(*outcomes))


def checkIfWin(tuple):
    currentpoints = copy(points)
    for i in tuple:
        if isinstance(i, int):
            currentpoints[i - 1] += 3
        else:
            currentpoints[int(i[0]) - 1] += 1
            currentpoints[int(i[2]) - 1] += 1
    nonfavteams_score = [currentpoints[i] for i in range(4) if i != favteam - 1]
    favteam_score = currentpoints[favteam - 1]
    for i in nonfavteams_score:
        if i >= favteam_score:
            return False
    else:
        return True


if __name__ == '__main__':
    UpdatePoints()
    NotPlayed()
    for i in GenerateOutcomes():
        if checkIfWin(i):
            counter += 1
    print(counter)