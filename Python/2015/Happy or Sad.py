# J2

str1 = input("Enter a string: ")

if len(str1) < 1 or len(str1) > 255:
    print("That is not a valid input.")
    exit()

happy = str1.count(":-)")
sad = str1.count(":-(")

if happy > sad:
    print("Happy")
elif happy < sad:
    print("Sad")
elif happy == -1 and sad == -1:
    print("None")
else:
    print("Unsure")
