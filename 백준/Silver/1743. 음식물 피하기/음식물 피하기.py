#백준 1743 음식물 피하기
from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,-1,1]

n, m, k = map(int,input().split()) 

lis = [[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,input().split())
    lis[a][b] = 1

visited = [[0]*(m+1) for _ in range(n+1)]

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    count = 1

    while queue :
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx <= 0 or nx >n or ny <= 0 or ny > m :
                continue
            if visited[nx][ny] == 1 or lis[nx][ny] == 0:
                continue
            if visited[nx][ny] == 0 and lis[nx][ny] == 1 :
                count +=1
                visited[nx][ny] = 1
                queue.append((nx,ny))
    return count

ans = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if lis[i][j] == 1 and visited[i][j] == 0:
            ans = max(ans, BFS(i,j))



print(ans)


