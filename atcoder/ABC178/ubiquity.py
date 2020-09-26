N = int(input())

res = 10 ** N - (2 * 9 ** N - 8 ** N)
res = res % ((10 ** 9) + 7)
print(res)