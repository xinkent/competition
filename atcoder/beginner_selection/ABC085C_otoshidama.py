#  https://atcoder.jp/contests/abs/tasks/abc085_c

N, Y = map(int, input().split())


p1 = 10000
p2 = 5000
p3 = 1000
max_p1 = int(Y / p1)

flg = False
n_list = (-1, -1, -1)
for n1 in range(0, max_p1+1):
    resi_1 = Y - n1 * p1
    max_p2 = int(resi_1 / p2)
    for n2 in range(0, max_p2+1) :
        if (n1 * p1 + n2 * p2 > Y) or (n1 + n2 > N):
            continue
        else:
            resi_2 = Y - n1 * p1 - n2 * p2
            n3 = int(resi_2 / p3)
        if n1 + n2 + n3 == N:
            n_list = (n1, n2, n3)
            flg = True
            break
    if flg:
        break

print("{} {} {}".format(n_list[0], n_list[1], n_list[2]))
        

