#백준 13164 행복유치원
from collections import deque
import sys
input = sys.stdin.readline


n, m =map(int,input().split())
lis = list(map(int,input().split()))

cost = 0
height = []
for i in range(1,n):
    height.append(lis[i]-lis[i-1])

height.sort()

q = deque(height)

for _ in range(m-1):
    q.pop()

print(sum(q))
    
