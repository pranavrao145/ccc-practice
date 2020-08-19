# J5

n = int(input())
a = input().split()
b = input().split()


def balanced(a, b):
    partner1 = ''
    partner2 = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            return False
        else:
            partner1 = b[i]
        for g in range(len(b)):
            if b[g] == a[i]:
                partner2 = a[g]
        if partner1 != partner2:
            return False
    return True


if balanced(a, b):
    print('good')
else:
    print('bad')
