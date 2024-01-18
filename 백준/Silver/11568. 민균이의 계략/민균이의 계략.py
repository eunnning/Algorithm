#백준 11568 민균이의 계략

import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))

dp = [1] * (n)

for i in range(n):
    for j in range(i):
        if lis[i] > lis[j] :
            dp[i] = max(dp[i],dp[j]+1)


print(max(dp))

    

