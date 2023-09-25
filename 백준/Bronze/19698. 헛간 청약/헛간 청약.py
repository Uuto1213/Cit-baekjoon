n, w, h, l = map(int, input().split())
a = w//l
b = h//l
c = a*b
if n <= c:
    print(n)
else:
    print(c)