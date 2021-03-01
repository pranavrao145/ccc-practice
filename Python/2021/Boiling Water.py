boilingPoint = int(input())

pressure = (5*boilingPoint) - 400

sea_level = int()

if pressure < 100:
    sea_level = 1
elif pressure > 100:
    sea_level = -1
else:
    sea_level = 0

print(pressure)
print(sea_level)