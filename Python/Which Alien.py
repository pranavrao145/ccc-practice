# 2011 J1

antenna = int(input("How many antennas?\n"))
eyes = int(input("How many eyes?\n"))

if antenna >= 3 and eyes <= 4:
    print("TroyMartian")

if antenna <= 6 and eyes >= 2:
    print("VladSaturnian")

if antenna <= 2 and eyes <= 3:
    print('GraemeMercurian')
