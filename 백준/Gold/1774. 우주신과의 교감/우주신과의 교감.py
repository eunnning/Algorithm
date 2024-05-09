#백준 1774 우주신과의 교감
import heapq
import math
import sys
input = lambda : sys.stdin.readline().strip()

n,m = map(int,input().split())
parent = [i for i in range(0,n+1)]

def find(x):
    if parent[x] != x :
        return find(parent[x])
    return x

def union(x,y):
    a = find(x)
    b = find(y)
    if a != b :
        if a > b :
            parent[a] = b
        else :
            parent[b] = a
        return True
    return False

god = []
for _ in range(n):
    god.append(list(map(int,input().split())))

for _ in range(m):
    i,j = map(int,input().split())
    union(i,j)

graph = []
for i in range(1,n):
    for j in range(i+1,n+1):
        if find(i) != find(j):
            x1,y1,x2,y2 = god[i-1][0],god[i-1][1],god[j-1][0],god[j-1][1]
            dist = math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
            heapq.heappush(graph,(dist,i,j))


cost = 0
while graph :
    dist, i,j = heapq.heappop(graph)
    if union(i,j):
        cost += dist

print(format(round(cost,2),".2f"))





    


