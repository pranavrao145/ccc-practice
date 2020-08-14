word = input().upper()
letters = 'IOSHZXN'
yesno = True

for i in word:
    if i not in letters:
        yesno = False
        break

if yesno:
    print('YES')
else:
    print('NO')