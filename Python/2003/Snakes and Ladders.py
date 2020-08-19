# J3

current_position = 1

while True:
    x = int(input("Enter the sum of the dice:\n"))
    if x < 2 or x > 12:
        print('You Quit!')
        break
    current_position += x
    if current_position == 54:
        current_position = 19
    elif current_position == 90:
        current_position = 48
    elif current_position == 99:
        current_position = 77
    elif current_position == 9:
        current_position = 34
    elif current_position == 40:
        current_position = 64
    elif current_position == 67:
        current_position = 86
    elif current_position > 100:
        current_position -= x
    print(f'You are now on square {current_position}')
    if current_position == 100:
        print('You Win!')
        break
