#백준 30024 옥수수밭
from collections import deque
import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
visited = [[0]*(m) for _ in range(n)]

heap = []
lis = []

for i in range(n):
    tmp = list(map(int,input().split()))
    lis.append(tmp)
    for j in range(m):
        if i == 0 or i == n-1 or j == 0 or j == m-1 :
            heapq.heappush(heap,(-tmp[j],i,j))
            visited[i][j] = 1

K = int(input())


dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []
cnt = 0
def BFS():
    global cnt
    while heap:
        if cnt == K :
            break
        cost, x,y =  heapq.heappop(heap)
        visited[x][y] = 1 
        ans.append((x,y))
        cnt += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx <n and 0<= ny <m and not visited[nx][ny] :
                heapq.heappush(heap,(-lis[nx][ny],nx,ny))
                visited[nx][ny] = 1
BFS()
for i,j in ans :
    print(i+1,j+1)

