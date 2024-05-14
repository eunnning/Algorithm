#백준 1261 알고스팟
import heapq
import sys
input = lambda : sys.stdin.readline().strip()

m,n = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().strip())))

distance = [[int(1e9)]*m for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dijkstra(i,j):
    queue = []
    heapq.heappush(queue, (0,i,j))
    distance[i][j] = 0
    visited[i][j] = 1
    while queue :
        dist, x,y = heapq.heappop(queue)
        if x== n-1 and y == m-1 :
            return
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
 
            if 0 > nx or 0> ny or nx >= n or ny >= m or distance[nx][ny] < dist or visited[nx][ny] == 1:
                continue
            if board[nx][ny] == 0 :
                distance[nx][ny] = dist
                visited[nx][ny] = 1
                heapq.heappush(queue,(dist,nx,ny))
            else :
                distance[nx][ny] = dist + 1
                visited[nx][ny] = 1
                heapq.heappush(queue,(dist+1,nx,ny))
                
dijkstra(0,0)
print(distance[n-1][m-1])