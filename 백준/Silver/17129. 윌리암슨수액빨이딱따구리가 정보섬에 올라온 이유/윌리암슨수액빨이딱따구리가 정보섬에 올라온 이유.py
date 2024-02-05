#백준 17129 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

lis = []
food = []

for _ in range(n):
    lis.append(list(map(int,input().strip())))

for i in range(n):
    for j in range(m):
        if lis[i][j] < 2:
            continue
        if lis[i][j] == 2:
            x, y = i, j
        if lis[i][j] >= 3:
            food.append((i,j))
        


dx = [-1,0,1,0]
dy = [0,-1,0,1]

aa = 0
ans = 0

def BFS(x,y):
    global dist, aa, ans
    tmp = 0
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue :
        xx,yy = queue.popleft()
        for k in range(4):
            nx = xx +dx[k]
            ny = yy +dy[k]
            if 0 > nx or nx >= n or 0 > ny or ny >= m or lis[nx][ny] == 1:
                continue
            if lis[nx][ny] in [3,4,5]:    
                dist[nx][ny] = dist[xx][yy]+1
                aa = lis[i][j]
                ans = dist[nx][ny]
                print("TAK")
                print(dist[nx][ny])
                exit()
            if visited[nx][ny] == 0 and lis[nx][ny] == 0 :
                visited[nx][ny] = 1
                dist[nx][ny]= dist[xx][yy]+1
                queue.append((nx,ny))
            



visited = [[0]*m for _ in range(n)]
dist = [[0]*m for _ in range(n)]
BFS(x,y)
    

if aa == 0:
    print("NIE")
