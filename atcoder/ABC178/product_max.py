a,b,c,d = map(int, input().split())

score_list = []

for x in (a,b):
    for y in (c,d):
        score = x * y
        score_list.append(score)

print(max(score_list))