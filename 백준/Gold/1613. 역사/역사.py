#백준 1613 역사
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

graph =[[1e9]* (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(k) :
    a,b = map(int, input().split())
    graph[a][b] = min(graph[a][b],1)

for i in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])


s = int(input())

for _ in range(s):
    a,b = map(int, input().split())
    if graph[a][b] != 1e9   :
        print(-1)
        continue
    elif graph[b][a] != 1e9 :
        print(1)
        continue
    print(0) 
    





