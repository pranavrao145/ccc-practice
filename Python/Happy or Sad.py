str1 = input("Enter a string: ")

if len(str1) < 1 or len(str1) > 255:
    print("That is not a valid input.")
    exit()

happy = 0
sad = 0


def f(x):
    global happy
    y = str1.split(":-)")
    happy = len(y) - 1
    return g()


def g():
    global sad
    z = str1.split(":-(")
    sad = len(z) - 1


if happy > sad:
    print("Happy")
elif happy < sad:
    print("Sad")
elif happy == -1 and sad == -1:
    print("None")
else:
    print("Unsure")
