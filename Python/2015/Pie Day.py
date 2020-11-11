n = int(input())
k = int(input())
ans = 0 

def pi(pieces, people, minimum):
    global ans
    if people == 1:
        ans += 1
        return
    for i in range(minimum, pieces//people + 1):
        pi(pieces - i, people - 1, i)

pi(n, k, 1)
print(ans)
