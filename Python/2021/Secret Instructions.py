instructions = []

while True:
    inp = input()
    if inp != "99999":
        instructions.append(inp)
    else:
        break

prev_direction = str()

for instruction in instructions:
    if instruction[0:2] == "00":
        print(prev_direction + " " + instruction[2:])
    else:
        direction_sum = int(instruction[0]) + int(instruction[1])
        if direction_sum % 2 == 0:
            print("right " + instruction[2:])
            prev_direction = "right"
        else:
            print("left " + instruction[2:])
            prev_direction = "left"
