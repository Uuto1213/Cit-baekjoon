k, n, m = map(int, input().split())
if m - k*n < 0:
    print((m-k*n)+2*(k*n-m))
else:
    print(0)