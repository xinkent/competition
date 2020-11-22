N = int(input())
al = list(map(int, input().split()))

sum1 = []
tmp_sum = 0
for i in range(N):
    tmp_sum += al[i]
    sum1.append(tmp_sum)

sum2 = []
max2 = []
tmp_sum = 0
tmp_max = 0
for i in range(N):
    tmp_sum += sum1[i]
    sum2.append(tmp_sum)

    if sum1[i] > tmp_max:
        tmp_max = sum1[i]
    max2.append(tmp_max)

tmp_max = 0
for i in range(N-1):
    res = sum2[i] + max2[i+1] 
    if res > tmp_max:
        tmp_max = res

# print(sum1)
# print(sum2)
# print(max2)
print(max(tmp_max, sum2[-1]))
