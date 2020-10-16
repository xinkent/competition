H, W = map(int, input().split())

masu = ["#" * (W+2)]
for _ in range(H):
    s = input()
    s_ = "#" + s + "#"
    masu.append(s_)
masu.append("#" * (W+2))

# print(masu)

res = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        if masu[i][j] == "#":
            continue
        else:
            if masu[i+1][j] == ".":
                res += 1
            if  masu[i][j+1] == ".":
                res += 1

print(res)
