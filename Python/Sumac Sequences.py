term1 = int(input())
term2 = int(input())

sequences = [term1, term2]
flag = 0
prevtermindex = 0
currenttermindex = 1

while flag == 0:
    a = sequences[prevtermindex] - sequences[currenttermindex]
    sequences.append(a)
    if a > sequences[currenttermindex]:
        flag = 1
    prevtermindex += 1
    currenttermindex += 1

print(len(sequences))
