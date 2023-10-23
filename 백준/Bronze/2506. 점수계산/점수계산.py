t = int(input())
l = list(map(int,input().split()))
sum = 0
y = 0
for i in range(t):
    if l[i] == 1:
        y += 1
    else:
        y = 0
    sum += y
print(sum)

