# J3

word = (input())
length1 = 0
sub_words = []


def reverse(x):
    return x[::-1]


def check(word1):
    if word1 == reverse(word1):
        return True
    else:
        return False


for i in range(len(word) + 1):
    for f in range(len(word) + 1):
        modiword = word[i:f]
        sub_words.append(modiword)

for i in sub_words:
    z = check(i)
    y = len(i)
    if z and y >= length1:
        length1 = len(i)


print(length1)
