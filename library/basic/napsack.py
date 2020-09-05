"""
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

    def dfs_solve(self):
        print(self.rec(0, W))


if __name__ == "__main__":
    N, W = map(int, input().split())
    wv = [ tuple(map(int, input().split())) for i in range(N)]
    solver = SimpleDFS(N, W, wv)
    solver.dfs_solve()
    

