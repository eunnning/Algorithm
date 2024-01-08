#백준 2468 안전영역
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

lis =[]
for _ in range(n):
    lis.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

maxx = max(map(max, lis))
count = 1


def BFS(i,x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        xx,yy = queue.popleft()
        for k in range(4):
            nx = xx+ dx[k]
            ny = yy+ dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue
            if visited[nx][ny] == 1:
                continue
            if lis[nx][ny] > i :
                queue.append((nx,ny))
            visited[nx][ny] = 1


for i in range(0,maxx):
    visited = [[0] * n for _ in range(n)]
    tmp = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0 and lis[x][y] > i:
                BFS(i,x,y)
                tmp += 1
    count=max(count,tmp)
    
print(count)



             

