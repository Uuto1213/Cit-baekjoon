import sys
input = sys.stdin.readline
x = int(input())
cit = []
for i in range(x):
    a = int(input())
    cit.append(a)
cit.sort()
for y in range(x):
    print(cit[y])
        