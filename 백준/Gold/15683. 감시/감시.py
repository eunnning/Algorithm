#백준 15683 감시
from copy import deepcopy
import sys
input = lambda : sys.stdin.readline().strip()

n,m = map(int,input().split())
board = []
cctv = []

for i in range(n):
    tmp = list(map(int,input().split())) # 0 빈칸, 1~5 cctv, 6 벽
    board.append(tmp)
    for j in range(m):
        if 1 <= tmp[j] <= 5 :
            cctv.append([i,j,tmp[j]])

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def check (x,y,dir):
    dir %= 4
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        x,y = nx,ny
        if  nx < 0 or ny < 0 or nx >= n or ny >= m : 
            return
        if board[nx][ny] == 6 :
            return
        if board[nx][ny] != 0 :
            continue
        board[nx][ny] = -1

ans = 1e9

def DFS(idx):
    global ans

    if idx == len(cctv):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0 :
                    cnt += 1    
        ans = min(ans,cnt)
        return
    

    x = cctv[idx][0]
    y = cctv[idx][1]
    cctvnum = cctv[idx][2]
    
    tmp = [[0]*8 for _ in range(8)]

    for dir in range(4):
        for i in range(n):
            for j in range(m):
                tmp[i][j] = board[i][j]
        
        if cctvnum == 1:
            check(x,y,dir)
        elif cctvnum == 2:
            check(x,y,dir)
            check(x,y,dir+2)
        elif cctvnum == 3 :
            check(x,y,dir)
            check(x,y,dir+1)
        elif cctvnum == 4 :
            check(x,y,dir)
            check(x,y,dir+1)
            check(x,y,dir+2)
        elif cctvnum == 5 :
            check(x,y,dir)
            check(x,y,dir+1)
            check(x,y,dir+2)
            check(x,y,dir+3)

        DFS(idx+1)

        for i in range(n):
            for j in range(m):
                board[i][j] = tmp[i][j]
        
DFS(0)
print(ans)










