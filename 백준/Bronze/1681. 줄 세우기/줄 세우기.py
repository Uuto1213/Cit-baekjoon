n, l = map(int, input().split())
l = str(l)
k = 1
possible = []

for i in range(n) :
  while True :
    count = 0

    for j in str(k) :
      if j == l :
        count += 1
      else :
        count = count
        
    if count == 0 :
      possible.append(k)
      k += 1
      break

    else :
      k += 1
      
print(max(possible)) 