import heapq

n, d = map(int, input().split())

graph = [[] for _ in range(d+1)]  
INF = int(1e9)
distance = [INF]*(d+1) 

for i in range(d):
    graph[i].append((i+1, 1))
    

for _ in range(n):
    x, y, z = map(int, input().split())
    if y > d:
        continue
    graph[x].append((y, z))

def dijkstra(c):
    q = []
    heapq.heappush(q, (0, c))
    
    distance[c] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)

print(distance[d])
