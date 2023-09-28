#백준 1937 욕심쟁이 판다
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(40000) # 안하면 재귀 에러 남 ;;

dx = [1,-1,0,0]
dy = [0,0,-1,1]

n = int(input())

lis = []
for _ in range(n):
    lis.append(list(map(int,input().split())))

dp =[[-1]*(n) for _ in range(n)]

def DFS(i,j):
    if dp[i][j] == -1 : # 방문표시
        dp[i][j] = 0
        for k in range(4):
            x = i+ dx[k]
            y = j+ dy[k]
            if 0 <= x < n and 0 <= y < n and lis[x][y] > lis[i][j]:
                dp[i][j] = max(dp[i][j], DFS(x,y))
    return dp[i][j] + 1

ans = 0 
for i in range(n):
    for j in range(n):
        ans = max(ans, DFS(i,j))


    
print(ans)

    

