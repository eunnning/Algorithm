#백준 2589 보물섬
from collections import deque
import sys
iuput = lambda : sys.stdin.readline().strip()


n,m = map(int,input().split())


graph = []

for _ in range(n):
    graph.append(list((input().strip())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(i,j):
    queue = deque()
    visited = [[-1]*(m) for _ in range(n)]
    queue.append((i,j))
    visited[i][j] = 0
    cnt = 0
    while queue :
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] == 'L':
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])
    
    return cnt

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            ans = max(ans, BFS(i,j))

print(ans)