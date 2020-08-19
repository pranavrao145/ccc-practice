# J2
from math import sqrt, floor

while True:
    pictures = int(input('Enter the number of pictures:\n\t'))
    if pictures == 0:
        break
    length = int(floor(sqrt(pictures)))
    width = int(pictures/length)
    print(f'Minimum perimeter is {2*length + 2* width} with dimensions {length} x {width}')
