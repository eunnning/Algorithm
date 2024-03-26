#백준 27945 슬슬 가지를 먹지 않으면 죽는다
import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int,input().split())
graph = []
parent = [ i for i in range(n+1)] 

for _ in range(m):
    u,v,t = map(int,input().split())
    if u < v :
        heapq.heappush(graph, (t,u,v))
    else :
        heapq.heappush(graph, (t,v,u))

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    a = find(x)
    b = find(y)
    if a == b:
        return False
    else :
        if parent[a] < parent[b]:
            parent[b] = a
        else :
            parent[a] = b
        return True
d = 1

while graph :
    t, u, v = heapq.heappop(graph)

    if d != t :
        break 
    if union(u,v) :
        d += 1

print(d)


