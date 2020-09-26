"""
高橋君はデータの加工が行いたいです。
整数 a,b,cと、文字列 sが与えられます。 
a + b + c の計算結果と、文字列 sを並べて表示しなさい。

# テストケース
## 入力
1
2 3
test

## 出力
6 test
"""

a = int(input())
b, c = map(int, input().split())
s = input()
print("{} {}".format(a + b + c, s))
 
