I, J = [],[]
n, m = map(int, input().split())
for i in range(n):
    i = list(map(int, input().split()))
    I.append(i)
for j in range(n):
    j = list(map(int, input().split()))
    J.append(j)
for k in range(n):
    for u in range(m):
        print(I[k][u]+J[k][u], end = " ")
    print()     
