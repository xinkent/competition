N, M = list(map(int, input().split()))
H_list = list(map(int, input().split()))
W_list = list(map(int, input().split()))

H_sorted = sorted(H_list)
H_dif = [H_sorted[i] - H_sorted[i-1] for i in range(1, N)]
H_dif_sum_even = []
tmp_sum = 0
for i in range(0, N-1, 2):
    # print(i)
    tmp_sum += H_dif[i]
    H_dif_sum_even.append(tmp_sum)

H_dif_sum_odd = []
tmp_sum = 0
for i in range(1, N, 2):
    tmp_sum += H_dif[i]
    H_dif_sum_odd.append(tmp_sum)


# 何番目に入るか計算
def get_order(w):
    i = 0
    while H_sorted[i] < w:
        i += 1
        if i == len(H_sorted):
            break
    return i


def dif_sum_even(w, order):
    # print(w, order)
    if order == 0:
        w_dif = abs(H_sorted[0] - w)
        odd_sum = H_dif_sum_odd[-1]
        return w_dif + odd_sum
    a = int(order/2 - 1)
    even_sum = H_dif_sum_even[a]
    odd_sum = H_dif_sum_odd[-1] - H_dif_sum_odd[a]
    w_dif = abs(H_sorted[order] - w)
    return odd_sum + even_sum + w_dif


def dif_sum_odd(w, order):
    a = int(order/2) - 1
    even_sum = H_dif_sum_even[a]
    odd_sum = H_dif_sum_odd[-1] - H_dif_sum_odd[a]
    w_dif = abs(H_sorted[order-1] - w)
    return odd_sum + even_sum + w_dif


res = 10 ** 12
for w in W_list:
    order = get_order(w)
    if order % 2 == 0:
        tmp = dif_sum_even(w, order)
    else:
        tmp = dif_sum_odd(w, order)
    if tmp < res:
        res = tmp

print(res)
