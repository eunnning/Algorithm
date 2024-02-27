#백준 11123 양한마리... 양두마리...
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    while queue :
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<= nx < h and 0<= ny < w and visited[nx][ny] == 0 and lis[nx][ny] == '#':
                visited[nx][ny] = 1
                queue.append((nx,ny))


T = int(input())
for _ in range(T):
    h,w = map(int,input().split())
    cnt = 0
    lis = []

    for _ in range(h):
        lis.append(list(input().strip()))
    
    visited = [[0]*w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and lis[i][j] == '#' :
                BFS(i,j)
                cnt+=1
    
    print(cnt)



    
