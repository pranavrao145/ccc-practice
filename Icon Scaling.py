# 2012 J3

k = int(input())
lines = ['*x*', ' xx', '* *']


def multiply(x):
    global k
    newstring = ''
    for i in x:
        newstring += i * k
    return newstring


for i in lines:
    for g in range(k):
        print(multiply(i))
