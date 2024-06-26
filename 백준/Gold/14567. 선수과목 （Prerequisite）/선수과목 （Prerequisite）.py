#백준 14567 선수과목

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[]for _ in range(n+1)]
indegree = [0] *(n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] +=1

def topology_sort():
    dp = [0]*(n+1)
    queue = deque()

    for i in range(1,n+1):
        if indegree[i] == 0 :
            queue.append(i)
            dp[i] = 1
    
    while queue :
        now = queue.popleft()

        for i in graph[now]:
            indegree[i] -=1
            dp[i] = dp[now] +1
            if indegree[i] == 0 :
                queue.append(i)
    
    print(*dp[1:])
    

topology_sort()

