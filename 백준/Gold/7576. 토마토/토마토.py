#백준 7576 토마토
from collections import deque
import sys
iuput = lambda : sys.stdin.readline().strip()

n,m = map(int,input().split())
lis = []
tomato = []
nothing = []
for i in range(m):
    tmp = list(map(int,input().split()))
    lis.append(tmp)
    for j in range(n):
        if tmp[j] == 1 :
            tomato.append((i,j))
        if tmp[j] == -1:
            nothing.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [[-1]*n for _ in range(m)]

def BFS(tomato,nothing):
    queue = deque(tomato)
    for i,j in tomato :
        visited[i][j] = 0
    for i,j in nothing :
        visited[i][j] = -int(1e9)
    while queue :
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == -1 :
                visited[nx][ny] = visited[x][y]+1
                queue.append((nx,ny))

BFS(tomato,nothing)

if sum(row.count(-1) for row in visited) == 0 :
    print( max(map(max, visited)))
else :
    print(-1)
    

    
