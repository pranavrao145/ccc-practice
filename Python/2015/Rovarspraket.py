# J3

str1 = input("Enter a string: ")
str2 = ""

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
nearestvowel = ["a", "a", "e", "e", "e", "i", "i", "i", "i", "o", "o", "o", "o", "o", "u", "u", "u", "u", "u", "u", "u"]
nearestconsonant = ["c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z","z"]

for i in str1:
    if i in consonants:
        iindex = consonants.index(i)
        str2 = str2 + i + nearestvowel[iindex] + nearestconsonant[iindex]
    else:
        str2 = str2 + i
        continue

print(str2)
