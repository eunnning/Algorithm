#백준 23757 아이들과 선물 상자
from queue import PriorityQueue
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

gifts = list(map(int,input().split()))

kids = list(map(int,input().split()))

queue = PriorityQueue()

for gift in gifts :
    queue.put(-gift)

for kid in kids :
    gift = -queue.get()
    if gift >= kid :
        gift -= kid
        queue.put(-gift)
    else :
        print(0)
        exit()

print(1)





