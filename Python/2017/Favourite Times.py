# J4

minutes = int(input())
count = 0
time = 1200

def main():
    global minutes, count, time
    for i in range(minutes):
        # add one to the time
        time += 1

        # checks to adjust timing if necessary (to next hour)
        if time == 1260:
            time = 100
        for a in range(1,12):
            if time == (a*100) + 60:
                time = (a+1) * 100
        
        time = str(time) # converts time to string to check length and do subscripts for comparisons

        # only two possibilities: time has 3 difits or 4 digits

        # if the time has 3 digits, checks if it's an arithmetic sequenc
        if len(time) == 3:
            x = int(time[0])
            y = int(time[1])
            z = int(time[2])
            if z - y == y - x:
                count += 1
            else:
                pass

        # if the time has 4 digits, checks if it's an arithmetic sequenc
        else:
            w = int(time[0])
            x = int(time[1])
            y = int(time[2])
            z = int(time[3])
            if z - y == y - x == x - w:
                count += 1
            else:
                pass

        # converting time back into an integer
        time = int(time)


if __name__ == "__main__":
    main()
    print(count)