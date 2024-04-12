#백준 마법사 상어와 파이어볼
import sys
import math
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n,m,k =map(int,input().split())
fireball = deque()
graph = [[[] for _ in range(n)] for _ in range(n)]


dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(m):
    r,c,p,s,d = map(int,input().split())
    fireball.append((r-1,c-1,p,s,d))

while k > 0:
    #print('=========')
    k -= 1
    length = len(fireball)
    # 격자 초기화 
    graph = [[[] for _ in range(n)] for _ in range(n)]     

    #1. 모든 파이어볼이 자신의 방향 d로 s만큼 이동 
    for i in range(length):
        x,y,p,s,d = fireball.popleft()
        #print(x,y,p,s,d)
        ny, nx = y + dy[d]*(s%n), x + dx[d]*(s%n)
        #print("next 위치 (n 보정 전) :",nx,ny)
        if nx < 0 :
            nx += n 
        if ny < 0 :
            ny += n 
        if nx > 0 :
            nx %= n
        if ny > 0  :
            ny %= n
        #print("next 위치 (n 보정 후) :",nx,ny)
        graph[nx][ny].append((p,s,d))

    #2. 이동이 끝난 뒤 파이어볼 정리 
    for i in range(n):
        for j in range(n):
            p,s,odd, even = 0,0,0,0
            #2-1. 파이어볼 합치기
            length = len(graph[i][j])
            #print("2 i,j,len : ",i,j,length)
            if length >= 2 :
                for a,b,c in graph[i][j]:
                    #print("2-1 질량, 속력, 방향:",a,b,c)
                    p += a
                    s += b
                    if c % 2 == 0 :
                        even +=1
                    else :
                        odd += 1
                p = int(p/5)
                s = int(s/length)
                #print("2-1 합쳐진 후 질량, 속력:",p,s)
                if p == 0 :
                    continue
                if even == length or odd == length : # 모두 짝수 or 홀수
                    for c in range(0,8,2):
                       fireball.append((i,j,p,s,c))
                       #print("합쳐진 파이어볼 최종 :",i,j,p,s,c)
                else :
                    for c in range(1,8,2):
                       fireball.append((i,j,p,s,c))
                       #print("합쳐진 파이어볼 최종 :",i,j,p,s,c)
            #2-2. 파이어볼이 하나인 경우 그냥 파이어볼에 넣음
            elif length == 1 :
                a,b,c = graph[i][j][0]
                #print("2-2 질량, 속력, 방향:",a,b,c)
                fireball.append((i,j,a,b,c))
    #print(fireball)

length = len(fireball)
mm = 0
for i in range(length):
    r,c,p,s,d = fireball.popleft()
    mm += p
print(mm)
