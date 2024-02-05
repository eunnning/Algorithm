#백준 타노스는 요세푸스가 밉다
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n,k = map(int,input().split()) # 청설모 수, 제거될 청설모 수

queue = deque()

for i in range(1,n+1):
    queue.append(i)

while queue :
    if k <= len(queue) :
        queue.append(queue.popleft())
        for i in range(k-1):
            queue.popleft()
    else :
        a = queue.popleft()
        break

print(a)
    
            


