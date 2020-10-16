N = int(input())
p_list = map(int, input().split())

flag = [0] * 200001

min_val = 0
for p in p_list:
    flag[p] = 1
    if min_val != p:
        print(min_val)
    else:
        while(flag[min_val] != 0):
            min_val += 1
        print(min_val)
        
            
    
