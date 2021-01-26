import numpy as np
H, W = list(map(int, input().split()))
mat = []
for h in range(H):
    li = list(map(int, input().split()))
    mat.append(li)

memo = np.ones((H, W)) * -1

