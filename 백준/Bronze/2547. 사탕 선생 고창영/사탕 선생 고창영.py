x = int(input())


for i in range(x):
    i = input()
    a = int(input())   
    s = 0                
    for i in range(a):
        e = int(input())
        s = s+e
    if s%a == 0:
        print("YES")
      
    else:
        print("NO")