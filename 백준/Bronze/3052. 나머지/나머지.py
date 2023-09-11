
x = []
for i in range(10):
    a = int(input())
    x.append(a%42)
x=set(x)
print(len(x))