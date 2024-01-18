#백준 10423 전기가 부족해
import heapq
import sys
input = sys.stdin.readline

n, m, k =map(int,input().split())

gragh = []
visited = [False] * (n+1)

elec = list(map(int,input().split()))

for _ in range(m):
    a,b,c =map(int,input().split())
    heapq.heappush(gragh, (c, a, b))

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b :
        return False
    else :
        if a == 0 :
            parent[b] = a
        else :
            parent[a] = b
        return True

queue =[[] for _ in range(n+1)]
parent = [ i for i in range(n+1)]
ans = 0 # 연결비용

for i in elec :
    parent[i] = 0

while gragh :
    cost, a, b = heapq.heappop(gragh)
    if union(a,b) :
        ans += cost
        queue[a].append((b,cost))
        queue[b].append((a,cost))
      
print(ans)

