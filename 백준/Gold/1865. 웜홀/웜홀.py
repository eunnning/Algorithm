#백준 1865 웜홀
import sys
input = lambda: sys.stdin.readline().rstrip()

def bf():
    distance[1] = 0
    k = len(graph)
    for i in range(n):
        for j in range(k):
            now,next,cost = graph[j]
            if distance[next] > distance[now] + cost:
                distance[next] = distance[now]+cost
                if i == n-1:
                    return print("YES")
    return print("NO")

T= int(input())
for _ in range(T):
    n,m,w = map(int,input().split())
    
    graph=[]
    distance = [int(1e9)]*(n+1)

    for _ in range(m):
        s,e,t = map(int,input().split())
        graph.append((s,e,t))
        graph.append((e,s,t))
    for _ in range(w):
        s,e,t = map(int,input().split())
        graph.append((s,e,-t))
    
    bf()

