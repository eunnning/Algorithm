#백준 16987 계란으로 계란치기
import sys
input = sys.stdin.readline

n = int(input())
lis = []

for _ in range(n):
    lis.append(list(map(int,input().split())))

answer = 0

def DFS(depth):
    global answer
    if depth == n :
        count = 0
        for i in range(n):
            if lis[i][0] <= 0 :
                count +=1
        answer = max(answer, count)
        return
    
    flag = False
    for i in range(n):
        if i == depth :
            continue
        if lis[depth][0] > 0 and lis[i][0] > 0 :
            lis[depth][0] -= lis[i][1]
            lis[i][0] -= lis[depth][1]
            flag = True
            DFS(depth+1)
            lis[depth][0] += lis[i][1]
            lis[i][0] += lis[depth][1]
    if not flag :
        DFS(depth+1)


DFS(0)
print(answer)
