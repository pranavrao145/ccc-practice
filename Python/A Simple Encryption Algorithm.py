# 2004 J4

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

code = {}
keyword = input().upper()
e = input().upper()
s = ''

for i in e:
    if i in alpha:
        s = s + i

print(s)

for i in keyword:
    code[i] = []


x = 0
y = 0

while x < len(keyword):
    y = x
    while y < len(s):
        code[keyword[x]].append(s[y])
        y += len(keyword)
    x += 1


for key in code:
    b = alpha.index(key)
    f = code.get(key)
    for i in range(len(f)):
        a = (alpha.index(f[i]) + b) % 26
        f[i] = alpha[a]


list1 = []

for key in code:
    list1.append(code.get(key))


flag = 0
h = len(list1)
string1 = ''

while len(string1) < len(s):
    z = flag % len(list1)
    q = list1[z]
    k = q.pop(0)
    string1 += k
    flag += 1

print(string1)
