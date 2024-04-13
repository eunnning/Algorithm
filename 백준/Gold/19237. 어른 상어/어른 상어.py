#백준 19237 어른 상어
import sys
from copy import deepcopy
input = lambda : sys.stdin.readline().strip()

n,m,k = map(int,input().split())

shark = [[[] for _ in range(n) ] for _ in range(n)]
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        shark[i][j] = [tmp[j],0,False] # 상어 숫자, 냄시
        if tmp[j] > 0 :
            shark[i][j][2] = True

dx = [-1,1,0,0] # 위, 왼쪽, 아래, 오른쪽
dy = [0,0,-1,1]

nowDir = list(map(int,input().split())) # 상어의 현재 방향
for i in range(m) :
    nowDir[i] -= 1

direction = [[[0]*4 for _ in range(4) ]for _ in range(m)]


for i in range(m): # 상어 : 1~m
    for j in range(4): # 방향 : 1~4
        tmp = list(map(int,input().split()))
        for z in range(4): 
            direction[i][j][z] = tmp[z] - 1

#1. 냄새 뿌리기
def spread(shark):
    newShark = deepcopy(shark)
    for i in range(n):
        for j in range(n):
            if 0 < newShark[i][j][0] <= m and newShark[i][j][2] == True :
                newShark[i][j][1] = k
    return newShark

#2. 상어 이동
def move(shark):
    newShark = deepcopy(shark)
    for i in range(n):
        for j in range(n):
            if  0 < shark[i][j][0] <= m and shark[i][j][2] : # 상어면 이동 가능
                sharkNum = shark[i][j][0] - 1
                nowdir = nowDir[sharkNum] 
                cnt = 0
                # 이동 방향 정하기
                while True :
                    x = direction[sharkNum][nowdir][cnt%4]
                    if cnt == 4 :
                        cnt = 0
                        shark, newShark = findNext(shark,newShark,i,j,sharkNum,nowdir,0)
                        break
                    # print("now i,j :",i,j,"now shark :",sharkNum+1,"next dir : ",x)
                    nx = i + dx[x] 
                    ny = j + dy[x] 
                    if 0<= nx < n and 0 <= ny < n and newShark[nx][ny][1] == 0 :
                        # print("next nx,ny : ",nx,ny)
                        if 0 < newShark[nx][ny][0] < sharkNum + 1 :
                            shark[i][j][2] = False
                            newShark[i][j][2] = False
                            # print("잡아 먹힌 상어", sharkNum + 1)
                            break
                        newShark[nx][ny][0] = sharkNum + 1
                        newShark[nx][ny][2] = True
                        shark[i][j][2] = False
                        newShark[i][j][2] = False
                        nowDir[sharkNum] = x
                        # print("new :",newShark[nx][ny])
                        break
                    cnt += 1
    
    return newShark

#2-1. 인접한 칸 중 냄시가 다 있을 경우
def findNext(shark,newShark,i,j,sharkNum,nowdir,cnt):
    while True :
        x = direction[sharkNum][nowdir][cnt]
        # print("now i,j :",i,j,"now shark :",sharkNum+1,"next dir : ",x)
        nx = i + dx[x] 
        ny = j + dy[x] 
        # print("next nx,ny : ",nx,ny)
        if 0<= nx < n and 0 <= ny < n :
            if  newShark[nx][ny][0] == (sharkNum+1) :
                newShark[nx][ny][0] = sharkNum + 1
                newShark[nx][ny][2] = True
                shark[i][j][2] = False
                newShark[i][j][2] = False
                nowDir[sharkNum] = x
                return shark, newShark
        cnt += 1


def smell(shark):
    newShark = deepcopy(shark)
    for i in range(n):
        for j in range(n):
            if 0 < newShark[i][j][1] and newShark[i][j][2] == False :
                newShark[i][j][1] -= 1
                if newShark[i][j][1] == 0 :
                    newShark[i][j][0] = 0
    
    return newShark

newShark = spread(shark)
for a in range(1,1001):
    newShark = move(newShark)
    # print('----move after----')
    # for i in range(n):
    #     print(newShark[i])
    newShark = spread(newShark)
    # print('----spread after----')
    # for i in range(n):
    #     print(newShark[i])
    newShark = smell(newShark)
    # print('----smell after----')
    # for i in range(n):
    #     print(newShark[i])
    # print(a,"번째 시뮬 결과  ")
    if sum(cell[2] for row in newShark for cell in row) == 1:
        print(a)
        exit()

print(-1)

