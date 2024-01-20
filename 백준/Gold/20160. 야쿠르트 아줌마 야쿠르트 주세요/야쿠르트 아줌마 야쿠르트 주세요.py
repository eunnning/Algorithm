#백준 20160 야쿠르트 아줌마 야쿠르트 주세요
import heapq
import sys
input = sys.stdin.readline

v,e = map(int,input().split())

graph = [[] for _ in range(v+100)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

yakult = list(map(int,input().split()))
start = int(input())

def dijkstra(x):
    queue = []
    distance = [1e9]*(v+100)
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

d1 = dijkstra(start)

n = len(yakult)

s = yakult[0]
time = 0
ans = 1e9

for node in yakult:
    d2 = dijkstra(s) # inf 0 1 11 111 1111 11111
    if d2[node] < 1e9 : # d2[1] = 1 < 1e9
        time += d2[node]  # 1
        s = node
        now = d1[node]
        if time >= now :
            ans = min(ans,node)


if ans < 1e9 :
    print(ans)
else :
    print(-1)




