# J5

from itertools import combinations

n = int(input())
lengths = list(map(int, input().strip().split()))

sums = [sum(combo) for combo in list(combinations(lengths, 2))]
occurences = dict()

for single_sum in sums:
    if not single_sum in occurences.keys():
        occurences[single_sum] = sums.count(single_sum)
        
widths = [value for value in occurences.values()]

max_width = max(widths)

print(max_width, widths.count(max_width))