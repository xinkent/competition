N = int(input())
ab_list = [list(map(int, input().split())) for _ in range(N)]


def calc(x1, x2):
    x1_ = x1 - 1 
    res = (x2 * (x2 + 1) / 2) - (x1_ * (x1_ + 1) / 2)
    return res


sum = 0
for ab in ab_list:
    a = ab[0]
    b = ab[1]
    sum += calc(a, b)

print(int(sum))