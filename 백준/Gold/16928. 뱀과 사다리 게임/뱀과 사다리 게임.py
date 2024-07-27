# 백준 16928 뱀과 사다리 게임
from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

n,m = map(int,input().split())

sadari  = dict()
bam  = dict()

board = [0]*101
visited = [0]*101

for _ in range(n):
    a,b = map(int,input().split())
    sadari[a] = b

for _ in range(m):
    a,b = map(int,input().split())
    bam[a] = b

queue = deque([1])

while queue :
    x = queue.popleft()
    if x == 100 :
        print(board[100])
        exit()
    for i in range(1,7):
        nx = x + i
        if nx <= 100 and not visited[nx]:    
            if nx in sadari.keys():
                nx = sadari.get(nx)
            
            if nx in bam.keys():
                nx = bam.get(nx)
            
            if not visited[nx] :
                visited[nx] = 1
                board[nx] = board[x] + 1
                queue.append(nx)


