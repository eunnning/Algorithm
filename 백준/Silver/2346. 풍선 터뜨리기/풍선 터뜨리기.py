# 백준 2346 풍선 터뜨리기
from collections import deque
n = int(input())
lis = list(map(int,input().split()))

q = deque()
for i in range(1,n+1):
    q.append(i)
ans =[]

ans.append(q.popleft())
tmp = lis[0]


while q :
    if tmp > 0 :
        while tmp != 0 :
            if tmp == 1:
                ans.append(q.popleft())
                break
            else :
                q.append(q.popleft())
                tmp -=1
    else :
        tmp = -tmp
        while tmp != 0 :
            if tmp == 1:
                ans.append(q.pop())
                break
            else :
                q.appendleft(q.pop())
                tmp -=1
    
    tmp = lis[ans[-1]-1]

for i in ans :
    print(i,end=" ")

