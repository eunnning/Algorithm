#백준 14502 연구소
import sys
from copy import deepcopy
from collections import deque
from itertools import combinations
input = lambda : sys.stdin.readline().strip()

n,m= map(int,input().split())
Map = []
viris = []
for i in range(n):
    tmp = list(map(int,input().split()))
    Map.append(tmp)
    for j in range(m):
        if tmp[j]== 2 :
            viris.append([i,j])

Case = [] 
for i in range(n):
    for j in range(m):
        if Map[i][j] == 0 :
            Case.append([i,j])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(newMap):
    queue = deque(viris)
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if 0 <= nx < n and 0<= ny <m and newMap[nx][ny] == 0 :
                newMap[nx][ny] = 2
                queue.append([nx,ny])
    return newMap
    

ans = 0
for tmp in combinations(Case,3):
    newMap = deepcopy(Map)
    for case in tmp :
        newMap[case[0]][case[1]] = 1

    newMap=BFS(newMap)
    cnt = sum(row.count(0) for row in newMap)
    if ans < cnt :
        ans = cnt
    
print(ans)