from typing import Dict, List

text = input("Enter a line of text: ")
list_of_elements: List[str] = text.split(" ")
print(text)
dict1: Dict[str, int] = {}

for i in list_of_elements:
    if dict1.get(i) is None:
        dict1[i] = 1
    else:
        dict1[i] = dict1[i] + 1
print(dict1)