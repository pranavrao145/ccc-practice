# J5

n = int(input())
a = input().split()
b = input().split()


def balanced(a, b):
    partner1 = ''
    partner2 = ''
    for i in range(n):
        if a[i] == b[i]: # goes through the first list and grabs the partner of the person in question for each loop
            return False
        else:
            partner1 = b[i] 
        for g in range(n): # goes through the second list to find the person in question and grabs their partner from there
            if b[g] == a[i]:
                partner2 = a[g]
        if partner1 != partner2: # if the person in question does NOT have the same partner in both lists, retrurns False right away 
            return False
    return True # if nothing fails and nobody is partnered with themselves and all partners are consistent, returns true


if balanced(a, b):
    print('good')
else:
    print('bad')
