#백준 1421 나무꾼 이다솜
import sys
input = sys.stdin.readline

n, c, w = map(int,input().split())

lis =[]

for _ in range(n):
    lis.append(int(input()))


money = 0
for i in range(1,max(lis)+1):
    total = 0
    for tree in lis :
        count = 0
        cost = 0
        count +=tree//i
        if tree % i == 0 :
            cost = tree//i - 1
        else :
            cost = tree//i 
        if (w * count * i - cost * c) > 0 :
            total += w * count * i - cost * c
    if total > money :
        money = total


print(money)



