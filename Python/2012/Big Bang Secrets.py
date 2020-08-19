# J4

k = int(input())
word = input().upper()

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
newstring = ''

for i in range(len(word)):
    index = alpha.index(word[i])
    shift = ((3 * (i + 1)) + k) % 26
    if shift < index:
        newstring += alpha[index - shift]
    else:
        newshift = shift - index
        newstring += alpha[-newshift]


print(newstring)