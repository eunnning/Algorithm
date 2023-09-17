#백준 17835 면접보는 승범이네
import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[]for i in range(n+1)] # 노드의 정보

for _ in range(m):
    u, v, c = map(int, input().split())
    graph[v].append((u,c))

space = list(map(int, input().split()))

def dijkstra():
    q=[]
    distance = [float('inf')]*(n+1)
    
    for i in space :
        heapq.heappush(q,(0,i))
        distance[i] = 0

    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] =cost
                heapq.heappush(q,(cost,i[0]))

    return distance    

idx = 0
maxx = 0

lis = dijkstra()


for i in range(1,n+1):
    if i not in space :
        if maxx < lis[i] :
            maxx = lis[i]
            idx = i


print(idx)
print(maxx)
