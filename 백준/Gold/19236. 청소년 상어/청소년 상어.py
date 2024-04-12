#백준 19236 청소년 상어
import sys
import copy 
input = lambda: sys.stdin.readline().rstrip()

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

fish = []
for i in range(4):
    a1,b1,a2,b2,a3,b3,a4,b4 = map(int, input().split())
    fish.append([[a1,b1-1],[a2,b2-1],[a3,b3-1],[a4,b4-1]])
eat = 0
maxx = 0

def move_fish(fish,shark_x, shark_y):
    newfish = copy.deepcopy(fish)
    #1. 물고기 이동
    for target in range(1,17):
        # print("target number : ",target)
        flag = False
        for i in range(4):
            if flag :
                break
            for j in range(4):
                #2. 이동할 물고기를 찾으면 물고기 이동시키기 
                if newfish[i][j][0] == target :
                    for _ in range(8):
                        #3. 바꿀 물고기 찾기
                        fishdir = newfish[i][j][1]
                        nx,ny = i + dx[fishdir], j + dy[fishdir]
                        #4. 바꿀 수 있다면
                        if 0<= nx < 4 and 0<= ny < 4 and not (nx == shark_x and ny == shark_y) :
                            # print("change:",newfish[i][j][0],newfish[nx][ny][0])
                            newfish[i][j][0],newfish[i][j][1],newfish[nx][ny][0],newfish[nx][ny][1] = newfish[nx][ny][0],newfish[nx][ny][1],newfish[i][j][0],newfish[i][j][1]
                            target += 1
                            flag = True
                            break
                        #5. 바꿀 수 없으면 바꿀 수 있을 때까지 방향 이동
                        else :
                            newfish[i][j][1] = (newfish[i][j][1] + 1) % 8
                if flag :
                    break
    return newfish
            

def move(fish,x,y,eat) :
    global maxx
    eat += fish[x][y][0]
    # print("현재eat",eat)
    # print("먹은 물고기 :",fish[x][y][0], "상어 방향",fish[x][y][1])
    fish[x][y][0] = 0
    #1. 물고기 이동
    newfish = move_fish(fish,x,y)
    # print(newfish)
    #6. 모든 물고기 바꾸면 상어 이동
    maxx = max(maxx, eat)
    sharkdir = newfish[x][y][1]
    for i in range(1,4):
        nx = x + dx[sharkdir]*i
        ny = y + dy[sharkdir]*i
        if 0 <= nx < 4 and 0 <= ny < 4 and newfish[nx][ny][0] > 0:
            # print("상어이동:",nx,ny)
            move(copy.deepcopy(newfish),nx,ny,eat) 

move(fish,0,0,0)
print(maxx)




