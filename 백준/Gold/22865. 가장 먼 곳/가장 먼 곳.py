#22865 백준 가장 먼곳
import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input()) # 자취 후보
a, b, c = map(int, input().split()) # 친구들 거리
m = int(input()) # 노드 정보

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((z,y))
    graph[y].append((z,x))

def sol(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance = [1e9]*(n+1)
    distance[start] = 0

    while queue :
        dist, now = heapq.heappop(queue)
        if dist > distance[now] :
            continue
        for case in graph[now] :
            cost = dist + case[0]
            if cost < distance[case[1]]:
                distance[case[1]] = cost
                heapq.heappush(queue,(cost,case[1]))

    return distance

maxx = -1
inx = -1

distance_a = sol(a)
distance_b = sol(b)
distance_c = sol(c)

for i in range(1,n+1):
    tmp = min(distance_a[i],distance_b[i],distance_c[i])
    if maxx < tmp:
        maxx = tmp
        idx = i

print(idx)
