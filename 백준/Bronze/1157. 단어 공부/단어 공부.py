a = input()
a = a.upper()

alp = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

b = []
for i in alp :
  b.append(a.count(str(i)))

m = max(b)
c = b.count(m)

if c >= 2 :
  print("?")

else :
  print(alp[b.index(m)]) 