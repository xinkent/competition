N = int(input())
al = list(map(int, input().split()))
max_a = max(al)

max_res = 0
max_k = 2
for i in range(2, max_a+1):
    res = 0
    for a in al:
        if a % i == 0:
            res += 1
    if res > max_res:
        max_res = res
        max_k = i


print(max_k)
