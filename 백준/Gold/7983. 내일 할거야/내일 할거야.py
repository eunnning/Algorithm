#백준 7983 내일할거야

import sys
input = sys.stdin.readline

n = int(input())
lis = []
maxx = 0
for _ in range(n):
    d, t = map(int,input().split())
    lis.append([d,t])
    maxx = max(maxx,t)

lis.sort(key= lambda x : -x[1])


holiday = maxx

for day, end in lis :
    if holiday >= end :
        holiday = end - day
    else :
        holiday -= day
        
print(holiday)


