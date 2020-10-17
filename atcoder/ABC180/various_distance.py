import numpy as np

N = int(input())
x_list = list(map(int, input().split()))

x_abs = list(map(abs, x_list))
print(sum(x_abs))

euc_dist = np.sqrt(sum(list(map(lambda x: x**2, x_list))))
print(euc_dist)

print(max(x_abs))