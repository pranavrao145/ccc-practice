# J3

year = int(input()) + 1


def check(x):
    s = str(x)
    for digit in s:
        if s.count(digit) > 1:
            return False
    return True


while not check(year):
    year += 1

print(year)
