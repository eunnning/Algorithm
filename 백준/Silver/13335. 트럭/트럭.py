# 백준 13335 트럭

from collections import deque

n, w, l = map(int, input().split()) # 트럭 수, 다리 길이, 최대하중

lis = list(map(int,input().split()))

queue = deque()
tmp = l
cnt = 0

for i in range (n) :
    if lis[i] <= tmp and cnt != w:
        queue.append(lis[i])
        tmp -=lis[i]
        if cnt != w :
            cnt +=1
    else : 
        for _ in range(w) :
            if cnt == w :
                tmp += queue[-w]
                if lis[i] > tmp :
                    queue.append(0)
                else :
                    queue.append(lis[i])
                    tmp -=lis[i] 
                    break
            else :
                queue.append(0)
                cnt+=1
            

print(len(queue)+w)
    

    
        
        
        