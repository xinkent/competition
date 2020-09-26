import numpy as np
import sys

MAX_INT = sys.maxsize

H, W = map(int, input().split())
ch, cw = [int(i) - 1 for i in input().split()]
dh, dw = [int(i) - 1 for i in input().split()]
S = [ [c for c in input()] for h in range(H)]

print(S)
score_memo = np.ones((H,W)) * -1
reached_memo = np.zeros((H,W))

walk_list = ((1, 0), (0, 1), (-1, 0), (0, -1))
warp_list = sum([[(i,j) for i in range(-2, 3) if (i,j) not in walk_list] for j in range(-2, 3)], [])
print(warp_list)
count = 0

def search_path(h, w, dh, dw, reached_memo): 
    """
    h,wから、dh, dwに到達するために必要な最小ワープ回数
    """
    reached_memo[h, w] = 1
    print("h, w {} {}".format(h, w))
    # print(reached_memo)

    # 既にメモ済みならそれを返す
    if score_memo[h, w] != -1:
        return score_memo[h, w]
    if h == dh and w == dw:
        score_memo[h, w] = 0
        # print("finish {} {}".format(h, w))
        # print(score_memo)
        return 0
    warp_num_list = [MAX_INT]
    # 歩き
    for delta_list in walk_list: 
        h_delta, w_delta = delta_list
        new_h, new_w = h + h_delta, w + w_delta
        if (0 <= new_h < H) and (0 <= new_w < W) and reached_memo[new_h, new_w] == 0:
            if S[new_h][new_w] == ".":
                print("new_h, new_w {} {}".format(new_h, new_w))
                warp_num = search_path(new_h, new_w, dh, dw, reached_memo)
                warp_num_list.append(warp_num)

    # ワープ
    for delta_list in warp_list:
        h_delta, w_delta = delta_list
        new_h, new_w = h + h_delta, w + w_delta
        if (0 <= new_h < H) and (0 <= new_w < W) and reached_memo[new_h, new_w] == 0:
            if S[new_h][new_w] == ".":
                reached_memo[new_h, new_w] = 1
                warp_num = search_path(new_h, new_w, dh, dw, reached_memo) + 1
                warp_num_list.append(warp_num)

    min_warp_num = min(warp_num_list)

    # スコアをメモ
    score_memo[h, w] = min_warp_num
    print("finish {} {}".format(h, w))
    print(warp_num_list)
    # print(score_memo)
    return min_warp_num


# reached = False
res = search_path(ch, cw, dh, dw, reached_memo)
# res = search_path(0,3,dh, dw, reached_memo)
# print("score_memo", score_memo)
if res == sys.maxsize:
    print(-1)
else:
    print(res)

