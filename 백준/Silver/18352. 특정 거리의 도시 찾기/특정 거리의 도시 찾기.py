#백준 18352 특정거리의 도시찾기
import heapq

n, m, k, x = map(int, input().split()) # n: 도시 개수, m: 도로 개수, k: 거리 정보, x: 출발 도시 번호

# 인접 리스트 초기화
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 출발 도시로부터의 최단 거리 계산
distance = [float('inf')] * (n + 1)
distance[x] = 0

queue = [(0, x)]

while queue:
    dist, node = heapq.heappop(queue)

    if dist > distance[node]:
        continue

    for neighbor in graph[node]:
        new_dist = dist + 1
        if new_dist < distance[neighbor]:
            distance[neighbor] = new_dist
            heapq.heappush(queue, (new_dist, neighbor))

# 거리가 k인 도시 출력
result = []
for i in range(1, n + 1):
    if distance[i] == k:
        result.append(i)

if not result:
    print(-1)
else:
    for city in result:
        print(city)
