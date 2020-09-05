"""
ビット全探索のチュートリアル

# 問題
値が違う 𝑛 個の数字が与えられます。選び方をすべての場合について考えたとき、
それぞれの場合で選んだ数値の和を、さらにすべて足して和を求めて下さい。

# テストケース
## 入力
4,10,1
## 出力
60 
"""

def bit_search(l):
    sum = 0
    for bit in range(1 << len(l)): # 0(0b000)から7(0b111)まで
        print("bit 10進数:{} 2進数: {:03b}".format(bit, bit))
        for i in range(len(l)):
            mask = 1 << i
            print("\t mask 10進数:{} 2進数: {:03b}".format(mask, mask))
            if bit & mask: # 右からi番目にビットが立っているかどうか判定
                sum += l[i]
    return sum

if __name__ == "__main__":
    l = list(map(int, input().split()))
    res = bit_search(l)
    print(res)