#백준 16568 엔비스카의 영혼
import sys
input = sys.stdin.readline

n, a, b = map(int,input().split())

dp = [1e9] * (n+1)
dp[n] = 0

for i in range(n,-1,-1):
    if i-1 >= 0 :
        dp[i-1] = min(dp[i]+1,dp[i-1]) 
    if i-a-1 >= 0 :
        dp[i-a-1] = min(dp[i]+1,dp[i-a-1]) 
    if i-b-1 >= 0 :
        dp[i-b-1] = min(dp[i]+1,dp[i-b-1]) 

print(dp[0])