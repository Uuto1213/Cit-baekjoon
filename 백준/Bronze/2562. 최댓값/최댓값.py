
a = []
for i in range(9):
    a.append(int(input()))
for j in range(0,9,1):
    if a[j] == max(a):
        print(a[j])
        print(j+1) 