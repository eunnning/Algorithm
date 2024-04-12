#백준 17144 미세먼지 안녕
import sys
from collections import deque
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip()

R,C,T = map(int, input().split())
dust = []
airup = []
airdown = []
for i in range(R):
    tmp = list(map(int,input().split()))
    dust.append(tmp)
    for j in range(C):
        if tmp[j] == -1 :
            if len(airup) == 0 :
                airup = [i,j]
            else :
                airdown = [i,j]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def spread(dust):
    newdust = [[0]* C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if dust[i][j] == 0 :
                continue
            if dust[i][j] == -1 :
                newdust[i][j] = -1
                continue
            cnt = 0
            # 인접한 네방향으로 확산
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                # 칸 안에 있으며, 공청기가 없는 경우 확산
                if 0 <= nx < R and 0 <= ny < C and dust[nx][ny] != -1 :
                    amount = dust[i][j] // 5
                    newdust[nx][ny] += amount
                    cnt += 1
            newdust[i][j] += dust[i][j] - amount*cnt

    
    return newdust

def aircleanerup(airup,dust):
    airx, airy = airup
    newdust = deepcopy(dust)
    # 미세먼지 이동
    for c in range(2,C):
        newdust[airx][c] = dust[airx][c-1] 
    newdust[airx][1] = 0
    for r in range(airx-1,-1,-1):
        newdust[r][C-1] = dust[r+1][C-1]
    for c in range(C-2,-1,-1):
        newdust[0][c] = dust[0][c+1]
    for r in range(1,airx):
        newdust[r][0]=dust[r-1][0]
    return newdust


def aircleanerdown(airdown,dust):
    airx, airy = airdown
    newdust = deepcopy(dust)
    # 미세먼지 이동
    for c in range(2,C):
        newdust[airx][c] = dust[airx][c-1] 
    newdust[airx][1] = 0
    for r in range(airx+1,R):
        newdust[r][C-1] = dust[r-1][C-1]
    for c in range(C-2,-1,-1):
        newdust[R-1][c] = dust[R-1][c+1]
    for r in range(R-2,airx,-1):
        newdust[r][0]=dust[r+1][0]
    return newdust
    

newdust = deepcopy(dust)

while T >= 1 :
    newdust = spread(newdust)
    newdust = aircleanerup(airup,newdust)
    newdust = aircleanerdown(airdown,newdust)
    T -=1

ans = 0
for r in range(R):
    for c in range(C):
        if newdust[r][c] > 0 :
            ans += newdust[r][c]

print(ans)