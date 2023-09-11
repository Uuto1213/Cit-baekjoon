n, m = map(int, input().split())

basket = list(range(n+1))

for _ in range(m):
    i, j = map(int, input().split())
    basket[i], basket[j] = basket[j], basket[i]

print(*basket[1:])