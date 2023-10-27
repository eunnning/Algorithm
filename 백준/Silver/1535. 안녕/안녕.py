#백준 1535 안녕

import sys
input = sys.stdin.readline

n = int(input())

cost = list(map(int,input().split()))
happy = list(map(int,input().split()))

lis = [(0,0)]
for i in range(n):
    lis.append((cost[i],happy[i]))

dp = [[0] * (101) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,101):
        if lis[i][0] < j :
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-lis[i][0]]+lis[i][1])
        else :
            dp[i][j] = dp[i-1][j]



print(dp[n][100])


