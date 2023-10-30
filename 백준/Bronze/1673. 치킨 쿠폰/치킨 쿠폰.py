import sys
input = sys.stdin.readline
try:
    while True:
        m, k = map(int, input().split())
        s = m
        sum = 0
        if k > m:
            print(m)
        else:
            while s - k >= 0:
                sum = sum + 1
                s = s - k
                s = s + 1
            print(m + sum )
except:
    exit()
    