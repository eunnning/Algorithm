#백준 18405 경쟁적 전염
from queue import PriorityQueue
from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, k = map(int,input().split())
lis = []
for _ in range(n):
    lis.append(list(map(int,input().split())))

s,x,y = map(int,input().split())

queue = deque()

for i in range(n):
    for j in range(n):
        if lis[i][j] != 0 :
            queue.append((lis[i][j],i,j))

viris = max(map(max,lis))
for _ in range(s):
    if not queue :
        print(lis[x-1][y-1])
        exit()
    tmp = sorted(list(queue))
    queue = deque(tmp)
    for _ in range(len(queue)) :
        a,b,c = queue.popleft()
        for m in range(4):
            nx = b + dx[m]
            ny = c + dy[m]
            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue
            if lis[nx][ny] == 0 :
                lis[nx][ny] = a
                queue.append((a,nx,ny))


print(lis[x-1][y-1])
