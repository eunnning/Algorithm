#백준 1245 농장관리
from collections import deque
dx = [0,0,1,-1,1,-1,-1,1]
dy = [1,-1,0,0,1,1,-1,-1]

n, m = map(int, input().split())

lis =[]
for _ in range(n):
    lis.append(list(map(int,input().split())))

ans = 0 # 산봉우리 개수
visited = [[0]*(m) for _ in range(n)]

def BFS(x,y):
    flag = True
    queue = deque()

    queue.append((x,y))
    h = lis[x][y]
    
    
    while queue:
        i,j = queue.popleft()
        for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 > nx or nx >= n or 0 > ny or ny >= m :
                continue 
            if lis[nx][ny] > lis[i][j] :
                flag = False
            if lis[nx][ny] != lis[i][j] :
                continue
            if visited[nx][ny] == 1 :
                continue
            
            queue.append((nx,ny))
            visited[nx][ny] = 1
    
    return flag 
    
                

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 :
            if BFS(i,j) == True:
                ans+=1



print(ans)
               

