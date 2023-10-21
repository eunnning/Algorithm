#백준 5972 택배배송
import heapq
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [1e9] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def di():
    queue = []
    heapq.heappush(queue,(0,1))
    distance[1] = 0

    while queue :
        dist, now = heapq.heappop(queue)
        if distance[now] < dist :
            continue
        for case in graph[now]:
            cost = case[1] + dist
            if cost < distance[case[0]]:
                distance[case[0]] = cost
                heapq.heappush(queue,(cost,case[0]))


di()

print(distance[n])
