x, n = map(int, input().split())
for i in range(x, x+n):
    if x % 2:
        x = x * 2
    else:
        x= x // 2
    x =x ^ 6
print(x)
            

