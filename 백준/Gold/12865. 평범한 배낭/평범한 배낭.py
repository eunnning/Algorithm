#백준 12865 평범한 배낭
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lis =[[0]]

for _ in range(n):
    w, v = map(int, input().split())
    lis.append([w,v])

lis.sort()



dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        w = lis[i][0]
        v = lis[i][1]
        if j < w :
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])    

    





