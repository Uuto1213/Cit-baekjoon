n = int(input())
a = list(map(int, input().split()))
m = max(a)
sum = 0
for i in range(n):
    sum += a[i]/m*100
print(sum/n)