n = int(input())

res = 0
for a in range(1, n):
    max_b = int((n-1)/a)
    res += max_b

print(res)