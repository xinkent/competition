T = int(input())
test_cases = [list(map(int, input().split())) for _ in range(T)]

# print(T)
# print(test_cases)

def sowa(x):
    if x < 0:
        return 0
    else:
        return x * (x+1) /2

def sowa2(x1, x2):
    return sowa(x2) - sowa(x1-1)

def all_count(N, x):
    res = (N - x + 1) ** 2 
    res %= 1000000007
    return res

def answer(N, A, B):
    a = max(A, B)
    b = min(A, B)
    all_a = all_count(N, a)
    all_b = all_count(N, b)

    count_list = []
    tmp = 0
    # for ax in range(N-a +1):
    #     bx_min = max(ax + 1 - b, 0)
    #     bx_max = min(ax + a -1, N-b)
    #     bx_count = bx_max - bx_min + 1
    #     tmp += bx_count

    dup_count = (N-a-b+2) * (N-b) + sowa2(N-b+1, N-1) - sowa(N-a-b+1) + (N-a+1)
    
    # dup_count = tmp ** 2
    dup_count %= 1000000007

    # print("all_a {}".format(all_a))
    # print("all_b {}".format(all_b))
    # print("dup_count {}".format(dup_count))
    return all_a * all_b - dup_count

for test_case in test_cases:
    N, A, B = test_case
    res = answer(N, A, B)
    res %= 1000000007
    print(res)