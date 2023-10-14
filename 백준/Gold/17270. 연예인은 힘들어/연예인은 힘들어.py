#백준 17270 연예인은 힘들어
import heapq
import sys
input = sys.stdin.readline

v,m = map(int,input().split())
graph = [[] for _ in range(v+1) ]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])


j,s =map(int,input().split())

for i in range(1,v+1):
    if len(graph[i]) == 0 :
        continue
    graph[i].sort()


INF= int(1e9)
distance_j = [INF]*(v+1) 
distance_s = [INF]*(v+1) 

def dijkstra_j(j):
    queue = []
    heapq.heappush(queue,(0,j))
    distance_j[j]=0
    while queue :
        dist , now = heapq.heappop(queue)
        if dist > distance_j[now] :
            continue
        for case in graph[now]:
            cost = case[0] + dist
            if cost < distance_j[case[1]]:
                distance_j[case[1]] = cost
                heapq.heappush(queue,(cost,case[1]))


def dijkstra_s(s):
    queue = []
    heapq.heappush(queue,(0,s))
    distance_s[s]=0
    while queue :
        dist , now = heapq.heappop(queue)
        if dist > distance_s[now] :
            continue
        for case in graph[now]:
            cost = case[0] + dist
            if cost < distance_s[case[1]]:
                distance_s[case[1]] = cost
                heapq.heappush(queue,(cost,case[1]))
dijkstra_j(j)
dijkstra_s(s)



minn = float('inf')
for i in range(1,v+1):
    if i == j or i == s :
        continue
    minn = min(minn, distance_j[i]+distance_s[i])
q=[] 
for i in range(1,v+1):
    if i == j or i == s :
        continue
    if distance_j[i]+ distance_s[i] != minn :
        continue
    if distance_j[i] > distance_s[i] :
        continue
    heapq.heappush(q,[distance_j[i]+ distance_s[i],distance_j[i],i])

if q :
    print(heapq.heappop(q)[2])
else :
    print(-1)
