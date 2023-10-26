#백준 2573 빙산
from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int,input().split())

lis = []

for _ in range(n) :
    lis.append(list(map(int,input().split())))


visited = [[0] * (m) for _ in range(n)]
board = [[0] * (m) for _ in range(n)]

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    while queue :
        a, b = queue.popleft()
        count = 0
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if lis[x][y] == 0 :
                count += 1
            if lis[x][y] > 0 and visited[x][y] == 0 :
                queue.append((x,y))
                visited[x][y] = 1
        board[a][b] = max(lis[a][b] - count, 0)


def check():
    tmp = 0
    for i in range(n):
        for j in range(m):
            if lis[i][j] > 0 :
                tmp +=1
    return tmp



ans = 0

for i in range(1,n-1):
    for j in range(1,m-1):
        if lis[i][j] > 0 :
            BFS(i,j)
            tmp = check()

            total_sum = sum(sum(row) for row in visited)

            if tmp > total_sum :
                print(ans)
                exit()
            else :
                ans += 1
                lis = copy.deepcopy(board)
                board = [[0] * (m) for _ in range(n)]
                visited = [[0] * (m) for _ in range(n)]
            
print(0)
            

        

