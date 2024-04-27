#백준 14889 스타트와 링크
from itertools import combinations
import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
lis = []
for _ in range(n):
    lis.append(list(map(int,input().split())))

a = [ i for i in range(n)]
m = n//2

power = []

for case in combinations(a,m) :
    tmp = 0
    for i in range(1,m):
        for j in range(i):
            tmp += lis[case[i]][case[j]] + lis[case[j]][case[i]]
    power.append(tmp)

ans = 1e9
k = len(power)//2
for i in range(k):
    tmp = abs(power[i] - power[-1-i])
    ans = min(tmp,ans) 

print(ans)




