R1, C1 = list(map(int, input().split()))
R2, C2 = list(map(int, input().split()))


COUNT = 0


def answer(r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return 0
    elif abs(r1 - r2) + abs(c1 - c2) <= 3:
        return 1
    elif (r1 + c1) == (r2 + c2):
        return 1
    elif (r1 - c1) == (r2 - c2):
        return 1
    else:
        if ((r2 + c2) - (r1 + c1)) % 2 == 0:
            return 2
        else:
            d = int(((r2 + c2) - (r1 + c1)) / 2)
            r1_mod = r1 + d
            c1_mod = c1 + d
            if abs(r1_mod - r2) + abs(c1_mod - c2) <= 3:
                tmp_a = 2
            else:
                tmp_a = 3
            
            d = int(((r2 - c2) - (r1 - c1)) / 2)
            r1_mod = r1 + d
            c1_mod = c1 - d
            if abs(r1_mod - r2) + abs(c1_mod - c2) <= 3:
                tmp_b = 2
            else:
                tmp_b = 3
            return min(tmp_a, tmp_b)
            


ans = answer(R1, C1, R2, C2)
print(ans)



