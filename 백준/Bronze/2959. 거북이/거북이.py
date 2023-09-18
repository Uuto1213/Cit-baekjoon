a,b,c,d= map(int, input().split())
hi = []
hi.append(a)
hi.append(b)
hi.append(c)
hi.append(d)
hi.remove(max(hi))
print(min(hi)*max(hi))