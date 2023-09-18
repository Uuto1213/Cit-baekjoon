L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A%C == 0:
    x = A//C
else:
    x = (A//C)+ 1
if B%D == 0:
    y = B//D
else:
    y = (B//D)+1
print(L- max(x,y))