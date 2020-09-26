import numpy as np
S = int(input())

memo = np.ones(S + 1) * -1

def dp(i):
    # print("i = {}".format(i))
    if memo[i] != -1:
        res = memo[i]
    elif i == 0 or i == 1 or i == 2:
        res = 0
    elif i == 3:
        res = 1
    else:
        sum = 1
        for j in range(i - 1, 2, -1):
            # if i == 5:
            #     print("    j = {}".format(j))
            if j <= i/2:
                tmp = max(dp(i-j) -1, 0)
            else:
                tmp = dp(i - j)
            if tmp != 0:
                sum += tmp
        res = sum
    memo[i] = res
    return res

for i in range(S):
    dp(i)
res = dp(S)
res = res % ((10 ** 9) + 7)
print(res)