#백준 6497 전력난
import heapq
import sys
input = sys.stdin.readline
while True :
    m, n = map(int,input().split())
    if  m == 0 and n == 0 :
        break
    graph = [[] for _ in range(m+1)]
    visited = [False] *(m+1)

    total = 0

    for _ in range(n):
        s,e,w = map(int,input().split())
        graph[s].append([w,e])
        graph[e].append([w,s])
        total += w


    answer = 0
    count = 0
    queue = [[0,0]]

    while queue :
        if count == m :
            break
        w, s = heapq.heappop(queue)
        if not visited[s] :
            visited[s] = True
            answer += w
            count += 1
            for i in graph[s] :
                if not visited[i[1]] :
                    heapq.heappush(queue, i)

    print(total - answer)

