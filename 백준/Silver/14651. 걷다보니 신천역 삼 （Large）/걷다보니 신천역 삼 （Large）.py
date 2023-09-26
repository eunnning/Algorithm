#백준 14651 걷다보니 신천역 삼(Large)
from itertools import product
import sys
input = sys.stdin.readline

n = int(input())

num = ['0','1','2']

if n == 1 :
    print(0)
    exit()
elif n == 2 :
    print(2)
    exit()
else :
    dp =[0]*(n+1)
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1]*3

print(dp[n]%1000000009)









