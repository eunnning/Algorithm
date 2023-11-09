#백준 2607 비슷한 단어

import sys
input = sys.stdin.readline

n = int(input())
a = input()
cnt = 0
for _ in range(n-1):
    b = input()

    #비슷
    a_list = list(a)
    b_list = list(b)
    a_list.sort()
    b_list.sort()

    if a_list == b_list :
        cnt +=1
        continue
    

    if len(a_list) >= len(b_list):
        a_sub_b = []
        for x in a_list :
            if x in b_list :
                b_list.remove(x)
            else :
                a_sub_b.append(x)
    else:
        a_sub_b = []
        for x in b_list :
            if x in a_list :
                a_list.remove(x)
            else :
                a_sub_b.append(x)
    

    
    if len(a_sub_b) <= 1 :
        cnt += 1


print(cnt)
