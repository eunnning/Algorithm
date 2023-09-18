import sys
import heapq

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,1,-1]
count = 0

while True:
    n = int(input())
    INF = int(1e9)
    if n == 0 :
        break
    count +=1

    graph = [] #노드 정보

    distance = [[INF]* n for _ in range(n)] # 최단 거리 배열
    
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    
    def dijkstra(x,y):
        q = []
        heapq.heappush(q,(graph[x][y],x,y))
        distance[x][y] = graph[x][y]

        while q :
            dist, nx, ny = heapq.heappop(q)

            if distance[nx][ny] < dist :
                continue
            for i in range(4):
                xx=dx[i]+nx
                yy=dy[i]+ny
                if (xx>=0 and xx<n and yy>=0 and yy<n):
                    cost = dist + graph[xx][yy]
                    if cost < distance[xx][yy] :
                        distance[xx][yy] = cost
                        heapq.heappush(q,(cost,xx,yy))
            
    dijkstra(0,0)
    
    print("Problem %d: %d"%(count, distance[n-1][n-1]))
    
    
    
    