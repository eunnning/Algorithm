#백준 7562 나이트의 이동
from collections import deque

def BFS(graph, x,y) :
    q = deque()
    q.append((x,y))
    graph[x][y]= 0
    

    while q :
        a,b = q.popleft()
    
        for k in range(8):
            nx = a + dx[k]
            ny = b + dy[k]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == -1:
                graph[nx][ny]=graph[a][b]+1
                
                q.append((nx,ny))



T =int(input()) # 테스트 케이스 개수 

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [2,1,-1,-2,-2,-1,1,2]


for i in range(T):
    N = int(input()) # 체스판 길이
    graph = [[ -1 for _ in range(N)] for _ in range(N)]
    
    
    x, y = map(int, input().split())  # 현재 있는 칸
    i, j = map(int, input().split())  # 이동하려고 하는 칸

    BFS(graph,x,y)

    print(graph[i][j])

