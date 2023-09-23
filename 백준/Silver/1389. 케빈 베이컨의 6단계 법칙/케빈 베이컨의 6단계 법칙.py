n, m = map(int, input().split()) # 유저의 수, 친구 관계의 수

INF = int(1e9)

graph = [[INF]*(n+1)for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i]= 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]= min(graph[i][j],graph[i][k]+graph[k][j])
cnt=[]

for i in range(1,n+1):
    tmp = 0
    for j in range(1,n+1):
        tmp+=graph[i][j]
    cnt.append(tmp)

ans = INF
idx = 0
for i in range(n):
    if ans > cnt[i]:
        ans = cnt[i]
        idx = i+1

print(idx)
    
        