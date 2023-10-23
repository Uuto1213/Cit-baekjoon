x = int(input())
for i in range(x):
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a = int(input()) 
    while a >= 25:
        a = a - 25          
        a1 = a1 + 1
    while a >= 10:
        a = a - 10 
        a2 = a2 + 1
    while a >= 5:
        a = a - 5
        a3 = a3 + 1
    while a >= 1:
        a = a - 1
        a4 = a4 + 1
    print(a1, a2, a3, a4)

