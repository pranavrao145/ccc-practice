dict1 = {}  # Dictionary

while True:
    list1 = input("Enter two words: ").split(" ")  # list for consideration
    if len(list1) == 1:
        check: str = list1[0]
        break
    else:
        dict1[list1[0]] = list1[1]
if dict1.get(check) is not None:
    print(f'The synonym for that word is {dict1[check]}.')
else:
    print("Sorry, that term is not in the dictionary.")