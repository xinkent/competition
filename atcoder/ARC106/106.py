import math
N = int(input())

def is_exp(x, flag):
    a = 3 ** flag
    while x >= a:
        if x == a:
            return flag
        else:
            flag += 4
            a = a * (3 ** 4)
    return -1



def answer(N):
    case_dict = {8:1, 4:2, 2:3, 6:4}
    first_num = int(str(N)[-1])
    if not (first_num in case_dict):
        return -1
    else:
        exp = 1
        while N > 5 ** exp:
            remain = N - 5 ** exp
            res = is_exp(remain, case_dict[first_num])
            if res != -1:
                return (res, exp)
                break
            exp += 1
    
    return(-1)


ans = answer(N)
if ans == -1:
    print(ans)
else:
    print(ans[0], ans[1])

