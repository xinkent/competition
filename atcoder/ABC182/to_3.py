import collections 


N = input()
N_str = [str(n) for n in N]
N_len = len(N_str)

N_mod = [int(n) % 3 for n in N]

c = collections.Counter(N_mod)

sum_N_mod = sum(N_mod)
if sum_N_mod % 3 == 0:
    print(0)
elif sum_N_mod % 3 == 1:
    if c[1] >= 1 and N_len > 1:
        print(1)
    elif c[2] >= 2 and N_len > 2:
        print(2)
    else:
        print(-1)
elif sum_N_mod % 3 == 2:
    if c[2] >= 1 and N_len > 1:
        print(1)
    elif c[1] >= 2 and N_len > 2:
        print(2)
    else:
        print(-1)
