x,y = map(int, input().split())
if 45<=y and y<= 59:
    print(x, y - 45)
else: 
    if x == 0:
        print(23, 60 +(y - 45))
    else:
        print(x - 1, 60 +(y - 45))