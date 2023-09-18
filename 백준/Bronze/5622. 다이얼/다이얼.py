dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
user = input()
total = 0
for i in user:
    for j in dial:
        if i in j:
            total += dial.index(j)+3
print(total)