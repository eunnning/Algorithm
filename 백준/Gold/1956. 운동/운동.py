#백준 1956 운동
import sys
input = lambda : sys.stdin.readline().strip()

n,m  = map(int,input().split())
road = [[1e9]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c  = map(int,input().split())
    road[a][b] = c 

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            road[i][j] = min(road[i][j], road[i][k] + road[k][j])
    

answer = 1e9
for i in range(1, n+1):
    answer = min(answer, road[i][i])
if answer == 1e9 :
    print(-1)
else :
    print(answer)