#백준 11501 주식
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))

    ans = 0  # 최대값 계산
    lis.reverse()
    maxx = lis[0]

    for i in range(1,n):
        if maxx < lis[i] :
            maxx = lis[i]
        else :
            ans += (maxx - lis[i])
        
    print(ans)


