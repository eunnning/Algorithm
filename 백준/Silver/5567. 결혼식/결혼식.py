#백준 5567 결혼식
from collections import deque

n = int(input())
m = int(input())


graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b))
    graph[b].append((a))

visited = []
friend = []


for i in graph[1]:
    visited.append(i)
    friend.append(i)

for i in visited:
    for j in graph[i] :
        if j not in friend and j != 1 :
            friend.append(j)

print(len(friend))






