# J3

added_times = [0, -300, -200, -100, 0, 100, 130]
cities = ["Ottawa", "Victoria", "Edmonton", "Winnipeg", "Toronto", "Halifax", "St. John's"]


def Local_Time(t, c):
    lt = t + c
    if lt > 2400:
        lt = lt - 2400
    elif lt < 0:
        lt = lt + 2400
    if lt % 100 >= 60:
        lt = (lt / 100 * 100 + 100) + (lt % 100 - 60)
    return lt


ottawatime = int(input("Enter the local time in Ottawa: "))

for i in range(len(cities)):
    print(f"{Local_Time(ottawatime, added_times[i])} in {cities[i]}.")

