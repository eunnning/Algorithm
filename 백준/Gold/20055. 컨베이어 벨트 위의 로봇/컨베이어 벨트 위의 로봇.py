#백준 20055 컨베이어 벨트 위의 로봇
import sys
from collections import deque
iuput = lambda : sys.stdin.readline().strip()

n,k = map(int,input().split())
lis = list(map(int,input().split()))

level = 0
queue = deque(lis)
robot = deque([False for _ in range(n)])

#1. 회전
def first():
    global queue
    global robot
    queue.rotate(1)
    robot.rotate(1)
    robot[0] = False
    robot[-1] = False

#2. 로봇 이동
def second():
    global queue
    global robot
    global n
    for i in range(n-1, 0, -1):
        if robot[i-1] and queue[i] > 0 and not robot[i] :
            robot[i] = True
            robot[i-1] = False
            queue[i] -= 1


#3. 로봇 올리기
def third() :
    global queue
    global robot
    if queue[0] > 0 :
        robot[0] = True
        queue[0] -= 1


while True :
    if queue.count(0) >= k :
        break
    first()
    second()
    third()
    level += 1

print(level)

