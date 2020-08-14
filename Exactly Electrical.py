# 2017 J3

pointA = list(map(int, input().strip().split()))
pointB = list(map(int, input().strip().split()))
charge = int(input())

distance = abs(pointA[0] - pointB[0]) + abs(pointA[1] + pointB[1])

if distance % 2 == charge % 2:
    print('Y')
else:
    print('N')
