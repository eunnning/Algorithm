#백준 14503 로봇 청소기
from collections import deque 
import sys
input = lambda : sys.stdin.readline().strip()

n,m = map(int,input().split())
startx, starty, dir = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]


board = []
visited = [[-1]*m for _ in range(n)]
for _ in range(n):
    board.append(list(map(int,input().split()))) # 0 빈칸, 1 벽
    
cnt = 1
def cleaner(startx,starty,dir):
    global cnt

    queue = deque()
    queue.append((startx,starty,dir))
    visited[startx][starty] = 1

    while queue :
        x, y, nd = queue.popleft()
        isclean = False

        for _ in range(4):
            nd = (nd + 3) % 4 
            nx = x + dx[nd]
            ny = y + dy[nd]
            if visited[nx][ny] == -1 and board[nx][ny] == 0 :
         
                visited[nx][ny] = 1
                cnt += 1
                isclean = True
                queue.append((nx,ny,nd))
                break

        if not isclean: 
            # 네 방향 모두 청소할 곳이 없으면 후진
            back_d = (nd + 2) % 4
            nx = x + dx[back_d]
            ny = y + dy[back_d]

            if board[nx][ny] == 0:
                queue.append((nx, ny, nd))
            else:
                return


cleaner(startx,starty,dir)
print(cnt)
        



