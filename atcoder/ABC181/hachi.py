s = input()
n = len(s)

count_dict = {}
for i in range(1, 11):
    count_dict[i] = 0
for s_char in s:
    count_dict[int(s_char)] += 1


def answer_1(s):
    if int(s) == 8:
        return True
    else:
        return False


def answer_2(s):
    if int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0:
        return True
    else:
        return False


def answer_3(s):
    for i in range(13, 125):
        x = 8 * i
        x_str = str(x)
        if '0' in x_str:
            continue
        tmp_count_dict = {}
        for i in range(1, 11):
            tmp_count_dict[i] = 0
        x0 = int(x_str[0])
        x1 = int(x_str[1])
        x2 = int(x_str[2])
        tmp_count_dict[x0] += 1
        tmp_count_dict[x1] += 1
        tmp_count_dict[x2] += 1

        if tmp_count_dict[x0] <= count_dict[x0] \
            and tmp_count_dict[x1] <= count_dict[x1] \
                and tmp_count_dict[x2] <= count_dict[x2]:
            return True

    return False


if len(s) == 1:
    ans = answer_1(s)
elif len(s) == 2:
    ans = answer_2(s)
else:
    ans = answer_3(s)

if ans:
    print("Yes")
else:
    print("No")
