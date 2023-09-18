#백준 1012 유기농배추
from collections import deque
import sys
input = sys.stdin.readline

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        i,j = queue.popleft()
        for k in range(4):
            xx = i + dx[k]
            yy = j + dy[k]
            if xx < 0 or xx >= m or yy < 0 or yy >= n :
                continue
            if visited[xx][yy] == 1 :
                continue
            if lis[xx][yy] == 1:
                visited[xx][yy] = 1
                queue.append((xx,yy))

T = int(input())
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for _ in range(T):
    m, n, k = map(int, input().split())
    lis = [[0] * n for _ in range(m)]
    for _ in range(k):
        a,b = map(int, input().split())
        lis[a][b] = 1
        visited =[[0] * n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if lis[i][j] == 1 and visited[i][j] != 1 :
                    BFS(i,j)
                    count+=1
    print(count)





