"""
# 参考
https://qrunch.net/@koralle/entries/QaGGA1m4l6NALqLX

# 概要
動的計画法を使う有名な問題です。以下のような問に答えます。

価値が 𝑣𝑖 、重さが 𝑤𝑖 で表される荷物が N 個ある。重さ B 
を超えないようにナップサックに入れる時、選んだ荷物の価値の合計は最大でどれだけか？

ここでは、AtCoder Beginner Contest 032 D – ナップサック問題 のデータセット 2 
に対応する部分点を得る解答を考えることとします。（つまり、N≦200 かつ全ての i(1≦i≦N) について 1≦wi≦1000 を満たす）

理解ができたら、問題の入力例と出力例を使って確認してみると良いでしょう。

# 入力
N W
w_1 v_1
...
w_n v_n

# テストケース
## 入力
10 2921
845　515936168 
325　981421680 
371　17309336  
112　788067075 
96　104855562
960　494541604 
161　32007355  
581　772339969 
248　55112800  
22　98577050 

## 出力
3657162058
"""

import time
import numpy as np

class SimpleDFS:
    """
    primitiveなDFS
    """
    def __init__(self, N, W, wv):
        self.N = N
        self.W = W
        self.wv = wv

    def rec(self, n, uplimit_w):
        ans = 0
        if n == N:
            return 0

        # n番目の品物を使えない場合
        if wv[n][0] > uplimit_w:
            return self.rec(n + 1, uplimit_w)

        # n番目の品物を使える場合
        else:
            ans = max(
                self.rec(n + 1, uplimit_w),
                self.rec(n+1, uplimit_w - wv[n][0]) + wv[n][1]
            )
            return ans 

    def solve(self):
        print(self.rec(0, W))

class MemoDFS:
    """
    メモ化DFS
    """
    def __init__(self, N, W, wv):
        self.N = N
        self.W = W
        self.wv = wv
        self.memo = np.zeros((self.N+1, self.W+1), dtype=int)

    def rec(self, n, uplimit_w):
        # 既に記録済みならその値を返す
        if self.memo[n, uplimit_w] > 0:
            return self.memo[n, uplimit_w]

        ans = 0
        if n == N:
            return 0

        # n番目の品物を使えない場合
        if wv[n][0] > uplimit_w:
            ans =  self.rec(n + 1, uplimit_w)

        # n番目の品物を使える場合
        else:
            ans = max(
                self.rec(n + 1, uplimit_w),
                self.rec(n+1, uplimit_w - wv[n][0]) + wv[n][1]
            )

        self.memo[n, uplimit_w] = ans
        return ans

class DP:
    """
    primitiveなDFS
    """
    def __init__(self, N, W, wv):
        self.N = N
        self.W = W
        self.wv = wv
        self.dp = np.zeros((self.N+1, self.W+1), dtype=int)

    def solve(self):
        for n in range(0,self.N):
            for w in range(self.W, -1, -1):
                # print(n, w)
                if w + self.wv[n+1, 0] > self.W:
                    self.dp[n+1, w] = self.dp[n, w]
                else:
                    self.dp[n+1, w] = max(self.dp[n, w], self.dp[n, w+self.wv[n+1,0]] + self.wv[n+1, 1])
                # print(self.dp)
        print(self.dp[N, 0])
        # print(self.dp)


if __name__ == "__main__":
    N, W = map(int, input().split())
    wv = np.array([[0,0]] + [ list(map(int, input().split())) for i in range(N)])
    start = time.time()

    # solver = SimpleDFS(N, W, wv)
    # solver = MemoDFS(N, W, wv)
    solver = DP(N, W, wv)
    solver.solve()

    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    

