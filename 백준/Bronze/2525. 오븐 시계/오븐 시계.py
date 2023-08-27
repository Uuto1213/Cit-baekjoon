x,y = map(int, input().split())
z = int(input())
s = x*60 + y + z
if s >= 1440:
    s = s - 1440
    print(s//60, s%60)
else: 
    print(s//60, s%60)