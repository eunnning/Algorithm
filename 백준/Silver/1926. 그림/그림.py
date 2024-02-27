
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())
lis = []

for _ in range(n):
    lis.append(list(map(int,input().split())))

visited = [[0]*(m) for _ in range(n)]
def BFS(i,j):
    queue = deque()
    visited[i][j] = 1
    queue.append((i,j))
    area = 1
    while queue :
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny <0 or nx >= n or ny >= m :
                continue
            if visited[nx][ny] == 1:
                continue
            if lis[nx][ny] == 1:
                visited[nx][ny] = 1
                area +=1
                queue.append((nx,ny))
    return area

maxx = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and lis[i][j] == 1:
            tmp = BFS(i,j)
            cnt +=1
            maxx = max(maxx,tmp)

print(cnt)
print(maxx)
                   

