import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

# 행, 열, 연료량 입력받기
n, m, power = map(int, input().split())

# 지도 입력받기
map_data = []
for _ in range(n):
    map_data.append(list(map(int, input().split())))

# 택시 초기 위치 입력받기
taxi_x, taxi_y = map(int, input().split())
taxi_x -= 1
taxi_y -= 1

# 승객 정보 입력받기
passengers = []
for _ in range(m):
    a, b, c, d = map(int, input().split())
    passengers.append((a - 1, b - 1, c - 1, d - 1))  

passengers.sort(key= lambda x: (x[0],x[1]))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(x,y):
    queue = deque()
    visited = [[-1]*n for _ in range(n)]
    queue.append((x,y))
    visited[x][y] = 1

    while queue :
        i,j = queue.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0<= ny < n and visited[nx][ny] == -1 and map_data[nx][ny] != 1 :
                visited[nx][ny] = visited[i][j] + 1
                queue.append((nx,ny))

    return visited
        
ans = 0
while True :
    if ans == m or power == 0:
        print(power)
        break
    #1. 택시랑 승객 사이 거리 찾기
    visited = BFS(taxi_x,taxi_y)
    min_dist = int(1e9) - 1
    for a,b,c,d in passengers:
        if (visited[a][b] -1) < min_dist and visited[a][b] > 0:
            next_sx, next_sy, next_ex,next_ey = a,b,c,d
            min_dist = visited[a][b] - 1
    # 택시가 어디는 못가는 경우
    if min_dist >= int(1e9) -1 :
        print(-1)
        break
    # 승객 태우러 가는 비용
    power -= min_dist 
    #print("승객까지 가는 비용 : ",min_dist,next_sx, next_sy, next_ex,next_ey)
    #2. 태워주기 
    visited = BFS(next_sx,next_sy)
    #print("목적지까지 이동 비용 :",visited[next_ex][next_ey]-1)
    if (visited[next_ex][next_ey]-1) > power or visited[next_ex][next_ey] == -1 :
        print(-1)
        break
    power += visited[next_ex][next_ey] - 1
    ans += 1
    taxi_x,taxi_y = next_ex,next_ey
    passengers.remove((next_sx, next_sy, next_ex,next_ey))


