#백준 17845 수강과목

import sys
input = sys.stdin.readline

n, k = map(int,input().split())

dp =[0] * (n+100)

lis = []
for _ in range(k):
    i, t = map(int,input().split())
    lis.append([i,t])

for i, t in lis :
    for m in range(n,t-1,-1):
        dp[m] = max(i+dp[m-t],dp[m])


print(dp[n])



