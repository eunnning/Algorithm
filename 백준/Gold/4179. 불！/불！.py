#백준 4179 불
from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,-1,1]

R, C = (map(int, input().split()))

lis =[]
for _ in range(R):
    lis.append(list(input().strip()))



def BFS(x,y):
    queue=deque()
    queue.append((x,y))
    if x == 0 or x == R-1 or y == 0 or y == C-1:
        print(1)
        exit()
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= R or ny < 0 or ny >= C :
                continue
            if visited[nx][ny] == -1:
                continue
            if visited[nx][ny] == 0 :
                visited[nx][ny] =visited[i][j]+1
                queue.append((nx,ny))
                
 
def FBFS():
    while fq :
        fx , fy = fq.popleft()
        for k in range(4):
            ffx = fx + dx[k]
            ffy = fy + dy[k]
            if ffx < 0 or ffx >= R or ffy < 0 or ffy >= C :
                continue
            if fvisited[ffx][ffy] == -1 :
                continue
            if fvisited[ffx][ffy] == int(1e9) :
                fvisited[ffx][ffy] = 1 + fvisited[fx][fy]
                fq.append((ffx,ffy))

        

        
        
        
visited = [[0]*C for _ in range(R)]
fvisited = [[int(1e9)]*C for _ in range(R)]

fq = deque()

for i in range(R):
    for j in range(C):
        if lis[i][j] == 'J' :
            x,y = i,j
            visited[i][j] = 1
        elif lis[i][j] == 'F' :
            fq.append((i,j))
            visited[i][j] = -1
            fvisited[i][j] = 1
        elif lis[i][j] == '#':
            visited[i][j] = -1
            fvisited[i][j] = -1



FBFS()
BFS(x,y)

ans = int(1e9)

for i in range(R):
    for j in range(C):
        if visited[i][j] < fvisited[i][j] and visited[i][j] > 1 and (i == 0 or i == R-1 or j == 0 or j == C-1) :
            ans = min(visited[i][j],ans)


if ans == int(1e9):
    print("IMPOSSIBLE")
else :
    print(ans)
