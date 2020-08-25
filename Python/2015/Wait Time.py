# J4

commands = int(input())
lines = []
people = []
temptimes = {}
finaltimes = {}
time = 0

for i in range(commands):
    x = input().split()
    x[1] = int(x[1])
    lines.append(x)

for line in lines:
    if line[0] == 'R':
        temptimes[line[1]] = time
        if line[1] not in people:
            people.append(line[1])
        time     += 1
    elif line[0] == 'W':
        time += (line[1] - 1)
    elif line[0] == 'S':
        if finaltimes.get(line[1]) is None:
            finaltimes[line[1]] = (time - temptimes.get(line[1]))
        else:
            finaltimes[line[1]] += (time - temptimes.get(line[1]))
        del temptimes[line[1]]
        time += 1

people.sort()

for person in people:
    if temptimes.get(person) is None:
        print(person, finaltimes.get(person))
    else:
        print(person, -1)




