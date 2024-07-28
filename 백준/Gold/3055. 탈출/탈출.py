#백준 3055 탈출
from copy import deepcopy
from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

r,c = map(int,input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

board = []

water_queue = deque()
hedgehog_queue = deque()

water_visited = [[-1] * c for _ in range(r)]
hedgehog_visited = [[-1] * c for _ in range(r)]

for i in range(r):
    tmp = list(input().strip())
    board.append(tmp)
    for j in range(c): 
        if tmp[j] == 'D':
            Dx,Dy = i,j
        elif tmp[j] == 'S':
            Sx, Sy = i,j
            hedgehog_queue.append((Sx, Sy))
            hedgehog_visited[Sx][Sy] = 0
        elif tmp[j] == '*':
            water_queue.append((i, j))
            water_visited[i][j] = 0

def spread_water():
    while water_queue:
        x, y = water_queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and water_visited[nx][ny] == -1 and board[nx][ny] == '.':
                water_queue.append((nx, ny))
                water_visited[nx][ny] = water_visited[x][y] + 1

def move_hedgehog():
    while hedgehog_queue:
        x, y = hedgehog_queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] == 'D':
                    print(hedgehog_visited[x][y] + 1)
                    return True
                if board[nx][ny] == '.' and hedgehog_visited[nx][ny] == -1:
                    if water_visited[nx][ny] == -1 or hedgehog_visited[x][y] + 1 < water_visited[nx][ny]:
                        hedgehog_queue.append((nx, ny))
                        hedgehog_visited[nx][ny] = hedgehog_visited[x][y] + 1
    return False

spread_water()
if not move_hedgehog():
    print("KAKTUS")

    