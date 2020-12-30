# J5
from itertools import chain, combinations

n = int(input())
invited = dict()

def powerset():
    s = [i for i in range(1, n)] # [1, 2, 3]
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

for i in range(n-1):
    inp = int(input())
    if inp in invited.keys():
        invited[inp].append(i + 1)
    else:
        invited[inp] = [i + 1]

combos = powerset()

for combo in powerset():
    for elem in combo:
        if elem in invited.keys():
            if not all(item in combo for item in invited[elem]):
                combos.remove(combo)

print(len(combos))
