s = input()
t = input()

def num_of_match(a,b):
    l = len(a)
    return sum([a[i] == b[i] for i in range(l)])


t_len = len(t)
nom_list = []
finish_flg = False
for i in range(len(s) - len(t) + 1):
    s_sub = s[i:i + t_len]
    nom = num_of_match(s_sub, t)
    num_mod = t_len - nom
    if num_mod == 0:
        print(0)
        finish_flg = True
        break
    else:
        nom_list.append(num_mod)

if not finish_flg:
    print(min(nom_list))

