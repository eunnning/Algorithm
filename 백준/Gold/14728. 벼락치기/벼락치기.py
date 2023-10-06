#백준 14728 벼락치기

import sys
input = sys.stdin.readline

n,t = map(int,input().split())

lis =[]

for _ in range(n):
    k,s = map(int,input().split())
    lis.append([k,s])

lis.sort(key= lambda x : -x[1])



dp = [0] * (t+1)



for time,score in lis :
    for i in range(t,time-1,-1):
        dp[i] = max(dp[i],dp[i-time]+score)
 


print(dp[t])
