#백준 27896 특별한 서빙
from queue import PriorityQueue
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

lis = list(map(int,input().split()))

cnt = 0 # 가지의 개수
tmp = 0 # 불만도

queue = PriorityQueue()

for i in lis :
    tmp += i 
    queue.put(-i)
    while tmp >= m :
        a = -queue.get()
        tmp -= (a * 2)
        cnt +=1

print(cnt)
