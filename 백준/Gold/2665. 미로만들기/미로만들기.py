#백준 2665 미로만들기
import heapq
import sys
input = lambda : sys.stdin.readline().strip()
n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int,list(input().strip()))))

INF = int(1e9)
distance = [[INF] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dikstra():
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
            if 0<= nx < n and 0<= ny < n :
                cost = dist 
                if board[nx][ny] == 0 :
                    cost += 1
                if cost < distance[nx][ny] :
                    distance[nx][ny] = cost
                    heapq.heappush(queue,(cost,nx,ny))

dikstra()
print(distance[n-1][n-1])