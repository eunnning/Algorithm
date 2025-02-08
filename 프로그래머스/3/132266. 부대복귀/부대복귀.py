from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = dict()

    for i in range(1,n+1):
        graph[i] = []

    for i,j in roads:
        graph[i].append(j)
        graph[j].append(i)
    
    distance = [-1]*(n+1)
    
    queue = deque()
    queue.append([destination,0])
    
    visited = set()
    
    while queue :
        node, dist = queue.popleft()
        
        if node in visited :
            continue
        
        visited.add(node)
        distance[node] = dist
        
        for i in graph[node] :
            queue.append([i, dist+1])
        
    
    for i in sources :
        answer.append(distance[i])
        
    return answer