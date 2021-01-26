N, X = list(map(int, input().split()))
S = input()

score = X

for s in S:
    if s == "o":
        score += 1
    if s == "x":
        score = max(score - 1, 0)

print(score)