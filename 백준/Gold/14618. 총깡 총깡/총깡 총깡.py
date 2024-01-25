#백준 14618 총깡총깡
import heapq
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

jhome = int(input()) # 진서집

k = int(input()) # 동물의 수

a = list(map(int,input().split())) # a형 집
b = list(map(int,input().split())) # b형 집

for _ in range(m) :
    x,y,z = map(int,input().split())
    graph[x].append((z,y))
    graph[y].append((z,x))

def dijkstra():
    queue =[]

    heapq.heappush(queue,(0,jhome))
    distance[jhome] = 0

    while queue :
        dist, node = heapq.heappop(queue)
        if dist > distance[node]: continue
        for case in graph[node]:
            cost = case[0] + dist
            if cost < distance[case[1]]:
                distance[case[1]] = cost
                heapq.heappush(queue,(cost,case[1]))



distance = [float('inf')]*(n+1)

dijkstra()

adist = float('inf')
bdist = float('inf')

for i in range(1,n+1):
    if i in a :
        if adist > distance[i]:
            adist = distance[i]
    elif i in b :
        if bdist > distance[i]:
            bdist = distance[i]

if adist == float('inf') and bdist == float('inf') :
    print(-1)
else :
    if adist <= bdist :
        print('A')
        print(adist)
    else :
        print('B')
        print(bdist)




