n = []
for j in range(1,31,1):
    n.append(j)
for i in range(28):
    a = int(input())
    if n.count(a) == 1:
        n.remove(a)
print(n[0])
print(n[1])