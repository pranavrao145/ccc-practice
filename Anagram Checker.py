# 2007 J4 Problem

characters = {}
characters2 = {}

phrase1 = input("Enter the first phrase: ").upper()
phrase2 = input("Enter the second phrase: ").upper()

for i in phrase1:
    if i not in characters:
        characters[i] = 1
    elif i == " ":
        continue
    else:
        characters[i] += 1

for i in phrase2:
    if i not in characters2:
        characters2[i] = 1
    elif i == " ":
        continue
    else:
        characters2[i] += 1

for key in characters2:
    if (characters.get(key) is None) or (characters.get(key) != characters2.get(key)):
        print("This is not an anagram. ")
        break
    else:
        print("This is an anagram.")
