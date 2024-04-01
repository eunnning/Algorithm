#백준 23061 백남이의 여행준비
import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
weight = [0]
values = [0]
for i in range(n):
    w,v = map(int,input().split())
    weight.append(w)
    values.append(v)

bags = [0]
for _ in range(m):
    bags.append(int(input()))

K = max(bags) 
dp = [[0]* (K+1)for _ in range(n+1)]

def sol(x):
    for i in range(1,n+1):
        for k in range(0,x+1):
            if weight[i] <= k  :
                dp[i][k] = max(dp[i-1][k],dp[i-1][k-weight[i]]+values[i]) 
            else :
                dp[i][k] = dp[i-1][k]
    


sol(K)
e=[]
for i in range(1,m+1):
    e.append((i,dp[n][bags[i]]/bags[i]))

e.sort(key= lambda x:-x[1])

print(e[0][0])