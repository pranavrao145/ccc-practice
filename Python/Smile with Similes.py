# 2004 J3

n = int(input())
m = int(input())
adjectives = []
nouns = []

for i in range(n):
    adjectives.append(input())

for i in range(m):
    nouns.append(input())

for i in adjectives:
    for g in nouns:
        print(f'{i} as {g}')
