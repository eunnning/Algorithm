#백준 21736 헌내기는 친구가 필요해
from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int,input().split())

lis =[]

for _ in range(n) :
    lis.append(list(input().strip()))

def BFS(i,j):
    cnt = 0
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    while queue :
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if visited[nx][ny] == 1 :
                continue
            if visited[nx][ny] == 0 and lis[nx][ny] == 'P':
                queue.append((nx,ny))
                visited[nx][ny] = 1
                cnt +=1
            elif visited[nx][ny] == 0 and lis[nx][ny] == 'O':
                queue.append((nx,ny))
                visited[nx][ny] = 1
    
    return cnt
    


for i in range(n):
    for j in range(m):
        if lis[i][j] == 'I':
            visited = [[0]* m for _ in range(n)]
            count = BFS(i,j)

if count == 0 :
    print('TT')
    exit()
print(count)