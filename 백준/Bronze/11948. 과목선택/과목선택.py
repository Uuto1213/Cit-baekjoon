l = []
g = []
a = l.append(int(input()))
b = l.append(int(input()))
c = l.append(int(input()))
d = l.append(int(input()))
e = g.append(int(input()))
f = g.append(int(input()))

l.remove(min(l))
g.remove(min(g))
print(sum(l)+sum(g))