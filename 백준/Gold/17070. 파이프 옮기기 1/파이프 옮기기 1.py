#백준 17070 파이프 옮기기1
import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
Map = []
for _ in range(n):
    Map.append(list(map(int,input().split())))

dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)] # 가로 세로 대각선

dp[0][0][1] = 1
for i in range(2,n):
    if Map[0][i] == 0 :
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1,n):
    for j in range(1,n):

        if Map[i][j] == 0 and Map[i-1][j] == 0 and Map[i][j-1] == 0 :
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1] #대각선
        
        if Map[i][j] == 0 :
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1] # 가로
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j] # 세로


    

print(sum(dp[i][n - 1][n - 1] for i in range(3)))
