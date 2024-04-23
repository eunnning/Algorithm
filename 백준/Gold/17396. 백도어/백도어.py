#백준 17396 백도어
import heapq
import sys
iuput = lambda : sys.stdin.readline().strip()


n,m = map(int,input().split())
enemy = list(map(int,input().split()))
maxx = sys.maxsize
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,cost = map(int,input().split())
    graph[a].append((cost,b))
    graph[b].append((cost,a))

distance = [maxx]*(1000001)

def sol(x):
    queue = []
    heapq.heappush(queue,(0,0))
    distance[0] = 0
    while queue :
        cost, now = heapq.heappop(queue)
        if distance[now] < cost :
            continue
        for case in graph[now]:
            dist = case[0] + cost
            if dist < distance[case[1]] and (not enemy[case[1]] or case[1] == n-1):
                distance[case[1]] = dist
                heapq.heappush(queue,(dist, case[1]))

sol(0)
if distance[n-1] < maxx:
    print(distance[n-1])
else :
    print(-1)
