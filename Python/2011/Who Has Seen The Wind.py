# J2

h = int(input())
M = int(input())


def Formula(t):
    global h
    A = -6 * (t ** 4) + h * (t ** 3) + 2 * (t ** 2) + t
    if A <= 0:
        return True
    return False


def AltitudeCheck():
    global M
    for i in range(1, M + 1):
        if Formula(i):
            print(f"The balloon first touches the ground at hour:\n{i}")
            return True
    return False


x = AltitudeCheck()

if not x:
    print("The balloon does not touch the ground in the given time.")
