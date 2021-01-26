import numpy as np

A, B, C = list(map(int, input().split()))
memo = np.ones((101, 101, 101)) * -1


def calc_ex(a, b, c, p, ll):
    coins = sorted([a, b, c])
    memo_score = memo[coins[0], coins[1], coins[2]]
    if memo_score != -1:
        return memo_score
    elif max(a, b, c) == 100:
        ex = p * ll
    else:
        ea = calc_ex(a+1, b, c, p * (a/(a+b+c)), ll+1)
        eb = calc_ex(a, b+1, c, p * (b/(a+b+c)), ll+1)
        ec = calc_ex(a, b, c+1, p * (c/(a+b+c)), ll+1)
        ex = ea + eb + ec
    memo[coins[0], coins[1], coins[2]] = ex
    return ex


ans = calc_ex(A, B, C, 1, 0)
print(ans)
