#백준 9694 무엇을 아느냐가 아니라 누구를 아느냐가 문제다
import heapq
import sys
input = sys.stdin.readline


T = int(input())
INF = int(1e9)

for k in range(T):
    n, m = map(int,input().split()) # n : 관계의 수 , m : 정치인 수
    graph = [[] for _ in range(m)]
    distance = [INF] * (m)
    lis = [-1] * m

    for _ in range(n):
        x,y,z = map(int,input().split())
        graph[x].append((y,z))
        graph[y].append((x,z))
    
    def dijkstra(start,end):
        queue = []
        heapq.heappush(queue,(0,start))
        distance[0] = 0
        while queue :
            dist, now = heapq.heappop(queue)
            if distance[now] < dist :
                continue
            for case in graph[now]:
                cost = case[1] + dist
                if cost < distance[case[0]]:
                    distance[case[0]] = cost
                    heapq.heappush(queue,(cost,case[0]))
                    lis[case[0]] = now
                    
        path=[]
        current = end
        while current != -1:
            path.append(current)
            current = lis[current]
        path.reverse()
        return path


    
    path = dijkstra(0, m-1)
    if distance[-1] >= INF :
        print("Case #%d: -1"%(k+1))
    else :
        print("Case #%d:"%(k+1),end=' ')
        for i in (path):
            print(i,end=' ')

    print()






