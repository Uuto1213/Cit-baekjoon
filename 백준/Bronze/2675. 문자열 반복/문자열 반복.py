s = int(input())
for i in range(s):
    a,b = map(str,input().split())
    a = int(a)
    b = list(b)
    for j in range(len(b)):
        print(b[j]*a, end = "")
    print()