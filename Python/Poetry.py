# 2003 J4

poems = int(input())
vowels = ['a', 'e', 'i', 'o', 'u']
finaloutput = []


def syllables(finalwords):
    global vowels
    finalsyllables = []
    for i in finalwords:
        latestindex = 0
        for g in range(len(i)):
            if i[g] in vowels:
                latestindex = g
        finalsyllables.append(i[latestindex:])
    return finalsyllables


def checkrelation(finalsyllables):
    if finalsyllables[0] == finalsyllables[1] == finalsyllables[2] == finalsyllables[3]:
        return 'perfect'
    elif finalsyllables[0] == finalsyllables[1] and finalsyllables[2] == finalsyllables[3]:
        return 'even'
    elif finalsyllables[0] == finalsyllables[2] and finalsyllables[1] == finalsyllables[3]:
        return 'cross'
    elif finalsyllables[0] == finalsyllables[3] and finalsyllables[1] == finalsyllables[2]:
        return 'shell'
    else:
        return 'free'


for i in range(poems):
    finalwords = []
    for f in range(4):
        z = input().split()
        finalwords.append((z.pop(len(z) - 1)).lower())
    finalsyllables = syllables(finalwords)
    finaloutput.append(checkrelation(finalsyllables))

for i in finaloutput:
    print(i)
