## 백준 1927 최소힙

import heapq 
import sys

input = sys.stdin.readline 

n = int(input())

heap = []

for _ in range(n):
    a = int(input())
    if a != 0 :
        heapq.heappush(heap,a)
    else :
        if not heap :
            print(0)
        else :
            print(heapq.heappop(heap))
        

