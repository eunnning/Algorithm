#백준 20529 가장 가까운 세 사람의 심리적 거리
import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    n = int(input())
    if n > 32 :
        lis = list((input().split()))
        print(0)
        continue
    lis = list((input().split()))
    cnt = []

    def distance(a,b):
        dist = 0
        for i in range(4): 
            if (a[i] != b[i]) :
                dist += 1
        return dist


    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                cnt.append((distance(lis[i],lis[j])+distance(lis[i],lis[k])+distance(lis[j],lis[k])))
    cnt.sort()
    print(cnt[0])
