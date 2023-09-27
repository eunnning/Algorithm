#백준 1504 특정한 최단경로
import heapq
import sys
input = sys.stdin.readline

n, e =map(int,input().split())

INF = int(1e9)
gragh = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(e):
    a,b,c = map(int,input().split())
    gragh[a].append((b,c))
    gragh[b].append((a,c))

v1,v2 = map(int,input().split())

lis1 =[1]
lis1.append(v1)
lis1.append(v2)
lis1.append(n)

lis2 =[1]
lis2.append(v2)
lis2.append(v1)
lis2.append(n)


def dijkstra(x):
    q = []
    heapq.heappush(q,(0,x))
    distance[x] = 0

    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in gragh[now]:
            cost = i[1] + dist
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
            
ans = 0
m = len(lis1)-1

tmp1 = 0
tmp2 = 0
for i in range(m) :

    distance = [INF]*(n+1)
    dijkstra(lis1[i])

    tmp1 += distance[lis1[i+1]]

for i in range(m) :

    distance = [INF]*(n+1)
    dijkstra(lis2[i])

    tmp2 += distance[lis2[i+1]]

ans = min(tmp1,tmp2)


if ans >= INF :
    print(-1)
else :
    print(ans)
