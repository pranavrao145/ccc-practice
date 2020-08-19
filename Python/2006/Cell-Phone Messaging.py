# J3

keys = {'abc': 2, 'def': 3, 'ghi': 4, 'jkl': 5, 'mno': 6, 'pqrs': 7, 'tuv': 8, 'wxyz': 9, '-': 0}
times = {'adgjmptw-': 1, 'behknqux': 2, 'cfilorvy': 3, 'sz': 4}

flag = 0
inputs = []

while flag == 0:
    string1 = input()
    if string1 != 'halt':
        inputs.append(string1.lower())
    else:
        flag = 1


def check(x):
    numberofiterations = 0
    for key in keys:
        if x in key:
            return numberofiterations
        numberofiterations += 1


def gettime(string):
    time = 0
    prevletter = ''
    global times
    for i in string:  # abba
        if prevletter == '':
            for key in times:
                if i in key:
                    time += times.get(key)
                    prevletter = i
        else:
            if i == prevletter or check(prevletter) == check(i):
                time += 2
                for key in times:
                    if i in key:
                        time += times.get(key)
                        prevletter = i
            else:
                for key in times:
                    if i in key:
                        time += times.get(key)
                        prevletter = i
    return time


for i in inputs:
    print(gettime(i))
