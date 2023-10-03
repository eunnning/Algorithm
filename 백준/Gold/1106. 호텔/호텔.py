#백준 1106 호텔

import sys
input = sys.stdin.readline

c, n = map(int,input().split())
lis=[]
for _ in range(n):
    lis.append(list(map(int,input().split())))

lis.sort()


dp = [1e9]*(c+100)
dp[0] = 0
people = lis[0][1]
cost = lis[0][0]

for i in range(1,people):
    dp[i] = cost

for cost, people in lis :
    for i in range(people,c+100):
        dp[i] = min(dp[i-people]+cost,dp[i])
      
print(dp[c])  



