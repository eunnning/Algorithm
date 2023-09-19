#백준 2644 촌수계산
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
m = int(input())
lis = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    lis[a].append(b)
    lis[b].append(a)



def BFS(a,count):
    queue = deque()
    queue.append((a,count))
    visited[a] = 1
    while queue :
        i, c = queue.popleft()
        for j in lis[i] :
            if j == y :
                return c+1
            if visited[j] != 1 :
                queue.append((j,c+1))
                visited[j] = 1

ans = BFS(x,0)
if ans == None :
    print(-1)
else :
    print(ans)





