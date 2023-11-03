#백준 22116 창영이와 퇴근
import sys
import heapq
input = sys.stdin.readline

n = int(input())

lis = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(n):
    lis.append(list(map(int, input().split())))


distance = [[1e9] * n for _ in range(n)]

def di():
    queue = []
    heapq.heappush(queue,(0,0,0))
    distance[0][0] = 0
    while queue :
        dist, x, y = heapq.heappop(queue)
        if dist > distance[x][y] :
            continue
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 > nx or 0 > ny or nx >= n or ny >= n :
                continue 
            cost = max(dist, abs(lis[nx][ny]-lis[x][y]))
            if distance[nx][ny] > cost :
                distance[nx][ny] = cost
                heapq.heappush(queue, (cost, nx,ny))

di()
print(distance[n-1][n-1])            

