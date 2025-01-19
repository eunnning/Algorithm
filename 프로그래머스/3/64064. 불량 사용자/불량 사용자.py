from itertools import permutations
def solution(user_id, banned_id):
    answer = 0
    
    n = len(user_id)
    m = len(banned_id)
    
    
    sett = set()
    lis = list()
    
    for per in list(permutations(user_id, m)) :
        flag1 = True # 한 쌍이 만족하는지 확인 flag
        for i in range(m):
            id1 = per[i] 
            id2 = banned_id[i]
            if not flag1 : # 만족하지 않으면 반복문 빠져 나오기
                break
            
            if len(id1) != len (id2) : # 길이가 다르면 반복문 빠져 나오기
                flag1 = False
                break
                
            else :
                k = len(id1) 
                flag2 = True
                for j in range(k) :
                    if id2[j] == '*' : # *는 통과
                        continue
                    elif id1[j] != id2[j] : # 알파벳이 다르면 x
                        flag2 = False
                        break
                if not flag2 :
                    flag1 = False
        
        if flag1 : 
            tmp = list(per)
            tmp.sort()
            tup = tuple(tmp)
            sett.add(tup)
            
    
    
    return len(sett)