x,y = map(int, input().split())

al = []
for i in range(x):
    a = list(map(int, input().split()))
    al.append(a)
al.sort(key = lambda x: (x[1],x[2],x[3]), reverse = True)

for i in range(x):
  if al[i][0] == y :
    index = i
for i in range(x):
  if al[index][1 : ] == al[i][1 : ] :
    print(i + 1)
    break 