#백준 11657 타임머신

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = []

distance = [(1e9)] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append((a,b,c))


def bf ():
    distance[1] = 0
    for i in range(n):
        for j in range(m):
            now = graph[j][0]
            next = graph[j][1]
            cost = graph[j][2]
            if distance[now] != 1e9 and distance[next] > distance[now] + cost :
                distance[next] = distance[now]+ cost
                if i == n - 1 :
                    return True

    return False
            

ans = bf()

if ans :
    print(-1)
else :
    for i in range(2,n+1):
        if distance[i] == 1e9 :
            print(-1)
        else :
            print(distance[i])