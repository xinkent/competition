N, S = input().split()
N = int(N)

pair_dict = {"A":"T", "T":"A", "C":"G", "G":"C"}

cnt_dict = {"A":0, "T":0, "C":0, "G":0}
list_dict = {"A":[0], "T":[0], "C":[0], "G":[0]}

for s in S:
    cnt_dict[s] = cnt_dict[s] + 1
    for d in ["A", "T", "C", "G"]:
        list_dict[d].append(cnt_dict[d])

# print(list_dict)

def check(i, j):
    A_cnt = list_dict["A"][j+1] - list_dict["A"][i]
    T_cnt = list_dict["T"][j+1] - list_dict["T"][i]
    C_cnt = list_dict["C"][j+1] - list_dict["C"][i]
    G_cnt = list_dict["G"][j+1] - list_dict["G"][i]
    if A_cnt == T_cnt and C_cnt == G_cnt:
        return True
    else:
        return False

res = 0
for i in range(len(S)):
    for j in range(i, len(S)):
        if check(i, j):
            res += 1

print(res)
