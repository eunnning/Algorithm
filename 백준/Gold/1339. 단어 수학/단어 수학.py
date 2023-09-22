#백준 1339 단어수학

import sys
input = sys.stdin.readline

n = int(input())
alpha = [0]* 26

for _ in range(n):
    lis = list(input().strip())
    lis.reverse()
    m = len(lis)
    k = 1
    for i in range (m):
        alpha[ord(lis[i])-65] += k
        k *=10



alpha.sort(reverse=True)

ans = 0
k = 9
for al in alpha :
    if al == 0 :
        break
    ans +=al * k
    k-=1

print(ans)

        
    