#백준 7569 토마토
from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

m,n,h = map(int,input().split())
tomato = []
board = [[[0] * m for _ in range(n)] for _ in range(h)]
visited = [[[-1]*m for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        tmp = list(map(int, input().split()))
        board[i][j] = tmp
        for k in range(m):
            if board[i][j][k] == 1:
                tomato.append((i, j, k))
            elif board[i][j][k] == -1:
                visited[i][j][k] = 0

dir = [(0,1,0),(0,0,1),(0,-1,0),(0,0,-1),(1,0,0),(-1,0,0)]
def BFS(tomato):
    queue = deque(tomato)
    for i,j,k in tomato :
        visited[i][j][k] = 0
    while queue :
        x,y,z = queue.popleft()
        for a in range(6):
            nx,ny,nz = x +dir[a][0],y +dir[a][1],z +dir[a][2]
            if 0 <= nx < h and 0<= ny <n and 0<= nz <m and visited[nx][ny][nz] == -1 and board[nx][ny][nz] == 0 :
                queue.append((nx,ny,nz))
                visited[nx][ny][nz] = visited[x][y][z] + 1

    
BFS(tomato)
if sum([visited[i][j].count(-1) for i in range(h) for j in range(n)]) == 0 :
    print(max(max(max(j) for j in i) for i in visited))
else :
    print(-1)
    

