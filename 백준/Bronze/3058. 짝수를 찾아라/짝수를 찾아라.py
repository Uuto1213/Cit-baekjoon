x = int(input())

for i in range(x):
    sum = 0
    even = []
    a = list(map(int, input().split()))
    for i in range(7):
        if a[i] % 2 == 0:
            sum = sum + a[i]
            even.append(a[i])
    print(sum, min(even))