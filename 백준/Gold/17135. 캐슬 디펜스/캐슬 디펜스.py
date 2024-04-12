#백준 17135 캐슬디펜스
import sys
from collections import deque
from copy import deepcopy
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

n,m,d = map(int, input().split())
nums = list(range(m))
enemy = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m) :
        if tmp[j] == 1:
            enemy.append([i,j])

def attack(newEnemy,a):
    global cnt,outlist
    distance = sys.maxsize
    tmp = [[0,0,m+1]]

    for idx, case in enumerate(newEnemy) :
        dist = abs(case[0]-n) + abs(case[1]-a)
        if dist <= d :
            if dist < distance :
                tmp = [[idx,case[0],case[1]]]
                distance = dist
            elif dist == distance :
                if tmp[0][2] > case[1] :
                    tmp = [[idx,case[0],case[1]]]

    if tmp[0][2] < m :
        tmp.sort(key= lambda x:(-x[1],x[2]))
        outlist.add(tmp[0][0])


        
# 적 이동
def moving(newEnemy):
    global outlist
    k = len(newEnemy)
    for i in range(k):
        if newEnemy[i][0] < n - 1 :
            newEnemy[i][0] += 1
        else :
            outlist.append(i)



def delete(outlist, newEnemy):
    outlist.sort(reverse=True)
    for i in outlist :
        del newEnemy[i]


ans = 0
#궁수 세명 배치
for a,b,c in combinations(nums,3):
    cnt = 0
    newEnemy= deepcopy(enemy)
    newEnemy.sort(key = lambda x:(-x[0],x[1]))
    while len(newEnemy) > 0 :
        #1. 적 공격
        outlist = set()
        attack(newEnemy,a)
        attack(newEnemy,b)
        attack(newEnemy,c)
        #1-1. 공격 맞은 적은 지우기
        cnt += len(outlist)
        delete(list(outlist), newEnemy)

        #2. 살아 남은 적 이동
        # print("mid enemy :",newEnemy)
        outlist = []
        moving(newEnemy)
        delete(outlist, newEnemy)

        
    ans= max(cnt,ans)

print(ans)



    

    
    

