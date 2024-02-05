#백준 17391 무한부스터
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n,m  = map(int,input().split())
lis = []
for _ in range(n):
    lis.append(list(map(int,input().split())))

visited = [[0]* m for _ in range(n)]

dx=[1,0]
dy=[0,1]

def BFS():
    queue = deque()
    queue.append((0,0,0))
    visited[0][0] = 1
    while queue :
        x,y,z = queue.popleft()
        power = lis[x][y]
        if x == n-1 and y == m-1 :
            return z
        for i in range(2):
            for j in range(1,power+1):
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                if nx < 0 or nx >= n or ny <0 or ny >= m :
                    continue
                if visited[nx][ny] == 1:
                    continue
                visited[nx][ny] = 1
                queue.append((nx,ny,z+1))
    
ans = BFS()

print(ans)
