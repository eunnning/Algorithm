#백준 1240 노드사이 거리
import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

lis = []
for _ in range(m):
    a,b = map(int,input().split())
    lis.append((a,b))


def BFS(start,end):
    queue = []
    heapq.heappush(queue,(0,start))
    distance = [1e9]*(n+1)
    distance[start] = 0

    while queue :
        dist, now = heapq.heappop(queue)
        if now == end :
            return distance
        if dist > distance[now] :
            continue
        for case in graph[now] :
            cost = case[0] + dist
            if cost < distance[case[1]]:
                distance[case[1]] = cost
                heapq.heappush(queue,(cost,case[1]))


    
for i,j in lis :
    distance = BFS(i,j)
    print(distance[j])
        

