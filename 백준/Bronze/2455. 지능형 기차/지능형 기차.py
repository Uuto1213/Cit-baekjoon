a1, a2 = map(int,input().split())
b1, b2 = map(int,input().split())
c1, c2 = map(int,input().split())
d1, d2 = map(int,input().split())

a = a2
b = a2 + b2 - b1
c = b + c2 - c1
d = c + d2 - d1

x = [a, b, c, d]
print(max(x))
