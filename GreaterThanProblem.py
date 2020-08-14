i = 0
counter = 0
prev_i = 0
flag = 0
while True:
    i = int(input("Enter a number: "))
    if flag == 0:
        prev_i = i
        flag = 1
        continue
    if i == 0:
        print(f'The number of numbers greater than the previous in this sequence is {counter}.')
        break
    else:
        if i > prev_i:
            counter += 1
    prev_i = i
