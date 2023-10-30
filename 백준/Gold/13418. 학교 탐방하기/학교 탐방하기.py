#백준 13418 학교탐방하기
import heapq
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

b_graph = [[] for _ in range(n+1)]
w_graph = [[] for _ in range(n+1)]


for _ in range(m+1):
    a,b,c = map(int,input().split())
    b_graph[a].append((-c,b))
    b_graph[b].append((-c,a))
    w_graph[a].append((c,b))
    w_graph[b].append((c,a))

for i in range(n+1):
    b_graph[i].sort()
    w_graph[i].sort()


def best():
    queue = []
    heapq.heappush(queue,(-1,0))
    count = 0 # 간선
    up = 0 # 오르막
    while queue :
        if count == n + 1 :
            break
        dist, now = heapq.heappop(queue)
        if visited[now] == 0:
            visited[now] = 1
            count += 1
            if dist == 0 :
                up += 1

            for case in b_graph[now]:
                if visited[case[1]] == 0 :
                    heapq.heappush(queue,case)
    return up

def worst():
    queue = []
    heapq.heappush(queue,(1,0))
    count = 0 # 간선
    up = 0 # 오르막
    while queue :
        if count == n + 1 :
            break
        dist, now = heapq.heappop(queue)
        if visited[now] == 0:
            visited[now] = 1
            count +=1
            if dist == 0 :
                up += 1

            for case in w_graph[now]:

                if visited[case[1]] == 0 :
                    heapq.heappush(queue,case)
    return up

visited = [0] * (n+1)
b_ans = best()
visited = [0] * (n+1)     
w_ans = worst()


print(w_ans**2 - b_ans**2)





