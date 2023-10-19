#백준 11559 puyo puyo
from collections import deque
import sys
input = sys.stdin.readline

lis = []
for _ in range(12):
    lis.append(list(input().strip()))


dx = [1,-1,0,0]
dy = [0,0,1,-1]

ans = 0

def BFS(i,j) :
    queue = deque()
    queue.append((i,j))
    same.append((i,j))
    visited[i][j] = 1
    while queue :
        a , b = queue.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if x < 0 or x >= 12 or y < 0 or y >= 6 :
                continue
            if visited[x][y] == 1 :
                continue
            if lis[i][j] == lis[x][y] and visited[x][y] == 0 :
                visited[x][y] = 1
                queue.append((x,y))
                same.append((x,y))



def delete():
    for i,j in same :
        lis[i][j] = '.'

def down():
    for i in range(6):
        for j in range(10,-1,-1):
            for k in range(11,j,-1):
                if lis[j][i] != '.' and lis[k][i] == '.' :
                    lis[k][i] = lis[j][i]
                    lis[j][i] ='.'
                    break


while 1 :
    flag = 0
    visited = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if lis[i][j] != '.' and visited[i][j] != 1:
                same = []
                BFS(i,j)
                if len(same) >= 4 :
                    delete()
                    down()
                    flag = 1
    if flag == 0 :
        break
    ans += 1

print(ans)   