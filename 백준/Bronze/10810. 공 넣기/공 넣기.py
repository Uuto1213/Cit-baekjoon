n, m = map(int, input().split()) 
b=[]
for i in range(n):
    b.append(0)
for j in range(m):
    x, y, z = map(int, input().split())
    for k in range(x,y+1):
        b[k-1]=z
print(*b)