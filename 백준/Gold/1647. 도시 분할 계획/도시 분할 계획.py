#백준 1647 도시분할계획
import heapq
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))


count = 0
ans = []
queue = [(0,1)]

while queue :
    if count == n :
        break
    cost, now = heapq.heappop(queue)
    if not visited[now]:
        visited[now] = True
        ans.append(cost)
        count += 1
        for i in graph[now]:
            if not visited[i[1]]:
                heapq.heappush(queue,i)

print(sum(ans)-max(ans))
