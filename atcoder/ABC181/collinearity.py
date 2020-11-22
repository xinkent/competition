N = int(input())
xy_list = [list(map(int, input().split())) for _ in range(N)]


def is_line(xy1, xy2, xy3):
    dx1 = xy2[0] - xy1[0]
    dx2 = xy3[0] - xy1[0]
    dy1 = xy2[1] - xy1[1]
    dy2 = xy3[1] - xy1[1]
    if (dx1 == 0 and dx2 == 0) or (dy1 == 0 and dy2 == 0):
        return True
    elif (dx1 != 0 and dx2 == 0) or (dx1 == 0 and dx2 != 0):
        return False
    elif (dy1 != 0 and dy2 == 0) or (dy1 == 0 and dy2 != 0):
        return False
    else:
        return dx1/dx2 == dy1/dy2


def answer(N, xy_list):
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                xy1 = xy_list[i]
                xy2 = xy_list[j]
                xy3 = xy_list[k]
                # print(xy1, xy2, xy3)
                if is_line(xy1, xy2, xy3):
                    return True
    return False


res = answer(N, xy_list)
if res:
    print("Yes")
else:
    print("No")