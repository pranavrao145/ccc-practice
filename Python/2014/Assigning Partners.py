# J5

num = int(input())
 
a, b, parters1, partners2, repeat = input().strip().split(), input().strip().split(), dict(), dict(), False

if __name__ == "__main__":
    for i in range(num):
        if a[i] == b[i]:
            repeat = True
            break

        parters1[a[i]] = b[i]
        partners2[b[i]] = a[i]

    if repeat or parters1 != partners2:
        print("bad")
    else:
        print("good")





