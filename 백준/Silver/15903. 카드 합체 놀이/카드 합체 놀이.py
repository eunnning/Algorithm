#백준 15903 카드 합체 놀이

import sys
import heapq
input = sys.stdin.readline

n,m = map(int, input().split())
lis = list(map(int,input().split()))

heapq.heapify(lis)

for _ in range(m) :
    a = heapq.heappop(lis)
    b = heapq.heappop(lis)

    heapq.heappush(lis, a+b)
    heapq.heappush(lis, a+b)

print(sum(lis))



