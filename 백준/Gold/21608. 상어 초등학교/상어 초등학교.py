#백준 21608 상어 초등학교
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
like = []
board = [[0]*n for _ in range(n)]

for i in range(n**2):
    x,a,b,c,d = map(int, input().split())
    like.append((x,a,b,c,d))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

#1. 좋아하는 학생이 인접한 칸에 많은지 체크
def like_space(x,y,a,b,c,d):
    global board
    cnt = 0
    for k in range(4):
        nx = x + dx[k] 
        ny = y + dy[k] 
        if 0<= nx < n and 0<= ny < n and board[nx][ny] in (a,b,c,d) :
            cnt +=1
    return cnt

#2. 비어있는 칸 체크
def empty_space(x,y):
    global board
    cnt = 0
    for k in range(4):
        nx = x + dx[k] 
        ny = y + dy[k] 
        if 0<= nx < n and 0<= ny < n and board[nx][ny] == 0 :
            cnt +=1
    return cnt

cnt = 0
while True:
    if cnt == n**2 :
        break
    for x,a,b,c,d in like :
        #print(x,a,b,c,d)
        like_cnt = 0
        candidate = []
        #1. 좋아하는 학생이 인접한 칸에 많은지 체크
        for i in range(n):
            for j in range(n):
                if board[i][j] != 0 :
                    continue
                like_tmp = like_space(i,j,a,b,c,d)
                empty_tmp = empty_space(i,j)
                if like_cnt < like_tmp :
                    like_cnt = like_tmp
                    candidate=[(i,j,empty_tmp)]
                elif like_cnt == like_tmp :
                    candidate.append((i,j,empty_tmp))
        if len(candidate) == 1:
            #print("조건 1 만족 :", candidate)
            i,j,empty = candidate[0]
            board[i][j] = x
            cnt += 1
            #print(board)
            continue
        # 조건 1 만족 못한 경우 비어있는 칸 중복 체크
        else :
            candidate.sort(key=lambda x:-x[2])
            tmp = []
            empty_cnt = candidate[0][2]
            #print(empty_cnt)
            for i,j,empty_tmp in candidate:
                if empty_tmp == empty_cnt :
                    tmp.append((i,j))
                else :
                    break
            if len(tmp) == 1 :
                #print("조건 2 만족 : ",tmp)
                i,j = tmp[0]
                board[i][j] = x
                cnt += 1
                #print(board)
                continue
            else :
                tmp.sort()
                #print("조건 3 만족 :",tmp)
                i,j = tmp[0]
                board[i][j] = x
                cnt += 1
                #print(board)


answer = 0
for x,a,b,c,d in like :
    idx = [(i, row.index(x)) for i, row in enumerate(board) if x in row]
    like_cnt = like_space(idx[0][0],idx[0][1],a,b,c,d)
    if like_cnt == 4 :
        answer += 1000
    elif like_cnt == 3 :
        answer += 100
    elif like_cnt == 2 :
        answer += 10
    elif like_cnt == 1 :
        answer += 1

print(answer)






        






