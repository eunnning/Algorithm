#백준 22352 항체 인식
from collections import deque
import sys
import copy
input = sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,m = map(int,input().split())

before = []
after = []

for _ in range(n):
    before.append(list(map(int,input().split())))
for _ in range(n):
    after.append(list(map(int,input().split())))

visited = [[0]*m for _ in range(n)]

def BFS(i,j,vaccine):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    copy_before[i][j] = vaccine
    while queue :
        a, b = queue.popleft()
        for k in range(4):
            x = a + dx[k] 
            y = b + dy[k]
            if x < 0 or x >= n or y < 0 or y >= m :
                continue
            if visited[x][y] == 1 :
                continue
            if visited[x][y] != 1 and before[x][y] == before[i][j] :
                copy_before[x][y] = vaccine
                visited[x][y] = 1
                queue.append((x,y))
    


if before == after :
    print("YES")
    exit()


for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j] :
            copy_before = copy.deepcopy(before)
            vaccine = after[i][j]
            BFS(i,j,vaccine)
            if copy_before == after :
                print("YES")
                exit()
            else :
                print("NO")
                exit()
            

