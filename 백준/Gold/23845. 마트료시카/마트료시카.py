#백준 23845 마트료시카
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
lis = list(map(int,input().split()))
m = [0] * 1000001

lis.sort()
cost = 0
for x in lis :
    m[x] += 1

for x in lis :
    if m[x]:
        m[x] -= 1
        Q, cnt = x, 1
        for j in range(x+1,1000001) :
            if m[j] :
                Q = j
                m[j] -= 1
                cnt += 1
            else :
                cost += Q * cnt
                break

print(cost)


