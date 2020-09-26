# import numpy as np

N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(K)]


S = []
for k in range(K):
    for i in range(LR[k][0], LR[k][1] + 1):
        S.append(i)
min_S = min(S)
memo = [-1 for _ in range(N)]

def move(x):
    res = -1
    if memo[x] != -1:
        res = memo[x]
        return res
    elif x < 0:
        res = 0
    elif x == 0:
        res = 1
    else:
        tmp = 0
        S_cand = [s for s in S if s <= x]
        for s in S_cand:
            if x-s == 0 or x-s >= min_S:
                tmp += move(x - s)
        res = tmp
    if x >= 0:
        memo[x] = res
    res %= 998244353
    return res

for i in range(min(10, N)):
    move(i)
res =  move(N - 1) % 998244353
print(res)
# print(memo)