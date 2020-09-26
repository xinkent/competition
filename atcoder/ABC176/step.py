N = input()
A = list(map(int, input().split()))

max_len = A[0]
sum = 0
# 前から順に調整
for ai in A:
    if ai < max_len:
        sum += max_len - ai
    else:
        max_len = ai

print(sum)