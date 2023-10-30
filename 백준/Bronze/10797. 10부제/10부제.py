cit = int(input())
sum = 0
a = list(map(int,input().split()))
for i in range(len(a)):
    if cit == a[i]:
        sum = sum + 1
print(sum)