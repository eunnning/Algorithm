#백준 16211 백채원
import heapq
from queue import PriorityQueue
import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

fan = list(map(int,input().split()))

def dijkstra(start):
    queue= []
    distance = [float('inf')]*(n+1)

    for x in start :
        heapq.heappush(queue,(0,x))
        distance[x] = 0

    while queue :
            dist, now = heapq.heappop(queue)
            if distance[now] < dist :
                continue
            for case in graph[now]:
                cost = case[1] + dist
                if cost < distance[case[0]]:
                    distance[case[0]] = cost
                    heapq.heappush(queue,(cost,case[0]))
    return distance

d1 = dijkstra([1])
d2 = dijkstra(fan)



ans = [i for i in range(2, n + 1) if d1[i] < d2[i]]

if not ans:
    print(0)
else:
    print(*ans)