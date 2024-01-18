#백준 20010 악덕영주혜유
import sys
import heapq
input = sys.stdin.readline

n, k = map(int,input().split())

graph = []

for _ in range(k):
    a,b,c =  map(int,input().split())
    heapq.heappush(graph, (c, a, b))



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
        parent[b] = a
        return True
#크루스칼
def kruskal():
    global ans
    ans = 0 # 연결비용
    while graph :
        cost, a, b = heapq.heappop(graph)
        if union(a,b) :
            ans += cost
            queue[a].append((b,cost))
            queue[b].append((a,cost))

    

def DFS(node, dist):
    global maxx
    global max_node
    visited[node] = True

    if maxx < dist :
        maxx = dist
        max_node = node

    for edge in queue[node]:
        if not visited[edge[0]]:
            DFS(edge[0],dist+edge[1])
    
parent = [ i for i in range(n+1)]
queue = [[] for _ in range(n+1)]
kruskal()

maxx = 0
max_node = 0
visited =[False]*(n+1)
DFS(0,0)

maxx = 0
visited =[False]*(n+1)
DFS(max_node,0)

print(ans)
print(maxx)

