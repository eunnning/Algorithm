#백준 2002 추월
import heapq
import sys
input = sys.stdin.readline

n = int(input())
lis = []
for i in range(n):
    lis.append(input())

cnt = 0
for i in range(n):
    tmp = input()
    if  lis[0] == tmp :
        del lis[0]
    else :
        cnt += 1
        lis.remove(tmp)

print(cnt)

        

