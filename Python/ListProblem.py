x = []
flag = 0
final = 0
len_list = 0
n = int(input("Give a number to end the sequence with: "))
while flag == 0:
    a = int(input("Enter a number to add to the list:"))
    if a == n:
        flag = 1
        len_list = len(x)
    else:
        x.append(a)
for i in range(len(x)):
    if i != 0 and i != len_list - 1:
        if x[i] < x[i + 1] < x[i + 2]:
            final +=1
    else:
        continue
print(final)