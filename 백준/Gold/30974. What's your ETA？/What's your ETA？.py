#백준 30974 What's your ETA
import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int, input().split())
code = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
inf = sys.maxsize

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

for i in range(1,n+1):
    graph[i].sort()

distance = [inf]*(n+1)

prime = [True] * (10000001)
k = int(10000001**0.5)
for i in range(2,k+1):
    if prime[i] == True:
        for j in range(i+i,10000001,i):
            prime[j] = False

def sol():
    queue = []
    heapq.heappush(queue,(0,1))
    distance[1] = 0
    while queue :
        cost, now = heapq.heappop(queue)
        if cost > distance[now]:
            continue
        for dist, next in graph[now]:
            primeNum = code[next-1]+code[now-1]
            if cost + dist < distance[next] and prime[primeNum]:
                distance[next] = cost + dist
                heapq.heappush(queue,(distance[next],next))

sol()
if distance[n] < inf:
    print(distance[n])
else :
    print('Now where are you?')

