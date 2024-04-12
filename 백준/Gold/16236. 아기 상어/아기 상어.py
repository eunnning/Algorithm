#백준 16236 아기상어
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
Map = []
fish =[]
for i in range(n):
    tmp = list(map(int,input().split()))
    Map.append(tmp)
    for j in range(n):
        if tmp[j] == 9:
            babyX,babyY = i,j
            Map[i][j] = 0
        elif 0 < tmp[j] <= 6 :
            fish.append([i,j,tmp[j]])

level = 2 # 상어 크기
eat = 0 # 먹은 물고기 수
times = 0 # 혼자 살아 남을 수 있는 시간

dx = [-1,0,1,0]
dy = [0,-1,0,1]

#1. 물고기 사이 거리 찾기
def BFS(babyX,babyY):
    queue = deque()
    queue.append((babyX,babyY))
    visited = [[-1]*n for _ in range(n)]
    visited[babyX][babyY] = 0
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0<= ny < n and visited[nx][ny] == -1 and Map[nx][ny] <= level:
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1

    return visited


#2. 먹을 수 있는 물고기 찾기
def findFish(visited):
    global eat,times,level,babyX,babyY
    tmp =[]
    short = sys.maxsize
    for i in range(n):
        for j in range(n):
            #2.1 아기 상어보다 크기가 작은 물고기 찾기
            if 0 < Map[i][j] < level :
                #2.2 거리 계산
                if  short > visited[i][j] > 0:
                    short = visited[i][j]
                    tmp = [i,j]
    
    if len(tmp) > 0 :
        eat += 1
        times += short
        Map[tmp[0]][tmp[1]] = 0
        babyX,babyY = tmp[0],tmp[1]
    else :
        return False
    
    if level == eat :
        level += 1
        eat = 0

    return True

flag = True
while flag :
    visited = BFS(babyX,babyY)
    flag = findFish(visited)
    # print("----- curr Map -----")
    # for i in range(n):
    #     print(Map[i])
    # print("curr times :",times)
    

print(times)





