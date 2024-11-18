#백준 26085 효규와 호구(easy)
from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
lis = []
for i in range(n):
    lis.append(list(map(int,input().split())))

one = 0
zero = 0

for i in range(n):
    for j in range(m):
        if lis[i][j] == 1 :
            one += 1
        else  :
            zero += 1

if one%2== 1 or zero %2 == 1:
    print(-1)
    exit()

for i in range(n):
    for j in range(m):
        now = lis[i][j] 
        for k in range(4):
            nx =  i + dx[k]
            ny =  j + dy[k]
            if  0<= nx < n and 0<= ny < m and lis[nx][ny] == now :
                print(1)
                exit()


print(-1)




    


