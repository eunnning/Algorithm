#백준 13424 비밀모임
import heapq
import sys
input = sys.stdin.readline

def dijkstra(i,person):
    queue = []
    heapq.heappush(queue,(0,person))
    distance[i][person] = 0
    while queue :
        dist, now = heapq.heappop(queue)
        if dist > distance[i][now] :
            continue
        for case in graph[now]:
            cost = case[1] + dist
            if cost < distance[i][case[0]]:
                distance[i][case[0]] = cost
                heapq.heappush(queue,(cost,case[0]))

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    INF =int(1e9)
    graph = [[] for _ in range(n+1) ]
    for _ in range(m):
        a, b, c = map(int,input().split())
        graph[a].append([b,c])
        graph[b].append([a,c])
    k = int(input()) # 모임 참여 친구 수
    distance = [[INF] * (n+1) for _ in range(k)] 
    friend = list(map(int,input().split()))

    lis=[0] * (n+1)
    for i in range(k):
        dijkstra(i,friend[i])
        for j in range(1,n+1):
            lis[j] += distance[i][j]


    minn = INF
    for j in range(1,n+1):
        if minn > lis[j] :
            minn = lis[j]
            ans = j

    print(ans)

        











