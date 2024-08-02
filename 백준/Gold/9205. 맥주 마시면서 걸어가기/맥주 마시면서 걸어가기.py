#백준 9205 맥주 마시면서 걸어가기
from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())

def BFS():
        queue = deque()
        queue.append((x1,y1))
        while queue :
            x,y = queue.popleft()
            if abs(x-x2) + abs(y-y2) <= 1000 :
                print('happy')
                return 
            for i in range(n):
                a,b = convenience[i]
                if not visited[i] :
                    if abs(x-a) + abs(y-b) <= 1000 :
                        visited[i] = 1
                        queue.append((a,b))
        
        print('sad')
        return

for _ in range(t):
    n = int(input())
    visited = [0]*n

    x1,y1 = map(int,input().split())

    convenience = []
    for _ in range(n):
        convenience.append(list(map(int,input().split())))
    
    x2, y2 = map(int,input().split())


    BFS()











