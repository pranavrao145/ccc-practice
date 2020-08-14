# 2009 J4 (Check and Understand)

from collections import deque

w = int(input())
message = deque(['WELCOME', 'TO', 'CCC', 'GOOD', 'LUCK', 'TODAY'])
while len(message) > 0:
    line = []
    while len(message) > 0 and len(''.join(line)) + len(line) + len(message[0]) <= w:
        line.append(message[0])
        message.popleft()
    spaces = [1] * (len(line) - 1)
    if len(line) == 1:
        spaces = [w - len(line[0])]
    else:
        i = 0
        while len(''.join(line)) + sum(spaces) < w:
            spaces[i % (len(line) - 1)] += 1
            i += 1
    for c, s, in zip(line, spaces + [0]):
        print(c + '.' * s, end='')
    print()
