# J4

tasks = [1, 2, 3, 4, 5, 6, 7]

# [  3, 5, 6 , 2, 1,  4, 7]
# [ 2, 1, 4, 7 3,  5, ]
flag = 0
flag1 = 0
# check to move it just before or after the required task. manipulate the original list

prereqs = {1: [2], 2: [], 3: [], 4: [1, 3], 5: [3], 6: [], 7: [1]}

pairs = []

currentpair = [0, 0]

while flag1 == 0:
    x = int(input())
    if flag % 2 == 0:
        currentpair[0] = x
        flag += 1
    else:
        currentpair[1] = x
        flag += 1
        if currentpair == [0, 0]:
            flag1 = 1
        else:
            pairs.append(currentpair)
            currentpair = [0,0]
print(pairs)

for i in pairs:
    if i[1] in prereqs.keys():
        (prereqs.get(i[1]).append(i[0]))
    else:
        prereqs[i[1]] = [[i[0]]]

print(prereqs)

for key in prereqs:
    if prereqs.get(key) == []:
        print(key, end=' ')
        for key1 in prereqs:
            if key in prereqs.get(key1):
                prereqs.get(key1).remove(key)








