X,Y,A,B = list(map(int, input().split()))


# 最初はA戦略
n_A = 0
while X < Y:
    if (X * (A-1) < B) and (X * A < Y):
        X *= A
        n_A += 1
    else:
        break

# 次はB戦略
if X + B >= Y:
    n_B = 0
else:
    tmp = int((Y-X) / B)
    if X + (tmp * B) >= Y:
        n_B = max(tmp - 1, 0)
    else:
        n_B = tmp

while X + n_B * B >= Y:
    n_B -= 1

i = 0
while True:
    if X + (n_B + i + 1) * B < Y:
        i+=1
    else:
        break
n_B += i
print(int(n_A + n_B))