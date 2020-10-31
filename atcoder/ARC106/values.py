import numpy as np

N, M = list(map(int, input().split()))
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

g = np.zeros((N, N))
for _ in range(M):
    c,d = list(map(int, input().split()))
    g[c-1][d-1] = 1
    g[d-1][c-1] = 1

def get_connected(N, g):
    stack = []
    # 0: 未訪問、 1: 訪問済み
    color = np.zeros(N)
    comp = [-1] * N
    for i in range(N):
        # print("i = {}".format(i))
        if color[i] == 0:
            stack.append(i)
            while(len(stack) > 0):
                # print("stack", end = "")
                # print(stack)
                v = stack.pop()
                color[v] = 1
                comp[v] = i
                for j in range(N):
                    # print("j == {}".format(j))
                    # print("g[i][j] = ".format(g[i][j]))
                    if g[v][j] == 1:
                        if color[j] == 0:
                            stack.append(j)

    return comp


def func1(lst, value):
    return [i for i, x in enumerate(lst) if x == value]

def answer(N, g, al, bl):
    # alの和とblの和が等しいことを確認
    if sum(al) != sum(bl):
        return("No")

    # 連結成分を番号づけ (1,1,1,2,2,2,1,...)
    # print(g)
    connect_list = get_connected(N, g)
    # print(connect_list)

    # 各連結成分について、目的達成可能かどうかをチェック
    connect_num = max(connect_list) + 1
    for cn in range(connect_num):
        target = func1(connect_list, cn)
        if len(target) == 0:
            continue
        a_sum = 0
        b_sum = 0
        for t in target:
            a_sum += al[t]
            b_sum += bl[t]
        if a_sum != b_sum:
            return("No")
    # 全ての連結成分について、達成可能であればYes、そうでなければNo
    return("Yes")

ans = answer(N, g, al, bl)
print(ans)