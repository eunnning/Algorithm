#백준 14496 그대, 그머가 되어
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

a,b = map(int,input().split())
n,m = map(int,input().split())

lis =[[] for _ in range(n+100)]
visited =[0]*(n+100)

for _ in range(m):
    i,j = map(int,input().split())
    lis[i].append(j)
    lis[j].append(i)

def BFS():
    queue = deque()
    queue.append((a,0))
    visited[a] = 1

    while queue:
        now, cnt = queue.popleft()
        if now == b :
            print(cnt)
            return
        for next in lis[now]:
            if visited[next] != 1:
                visited[next]= 1
                queue.append((next,cnt+1))
    return print(-1)

BFS()

