import sys
input = sys.stdin.readline
n = int(input())

lis = [list(map(int, input().split())) for _ in range(n)]

dp =[0]* (n+1)
tmp = n
for i in range(n-1,-1,-1):
    if lis[i][0] + i <= tmp:
        dp[i] = max(lis[i][1]+dp[i+lis[i][0]],dp[i+1]) 
    else :
        dp[i] = dp[i+1]
print(max(dp))