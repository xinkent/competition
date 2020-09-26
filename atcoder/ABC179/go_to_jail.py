n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
flg = False
for i in range(n):
    if d[i][0] == d[i][1]: # ゾロ目だったらカウントを進める
        cnt += 1
    else: # ゾロ目じゃなかったらカウントを0に戻す
        cnt = 0
    if cnt >= 3:
        flg = True
        break

if flg:
    print("Yes")
else:
    print("No")