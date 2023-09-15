# 백준 15787 기차가 어둠을 헤치고 은하수를
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

train = [[0]*22 for _ in range(n+1)]

for _ in range(m):
    lis = list(map(int, input().split()))
    if lis[0] == 1 :
        if train[lis[1]][lis[2]] == 0 :
            train[lis[1]][lis[2]] = 1
    elif lis[0] == 2 :
        if train[lis[1]][lis[2]] == 1:
            train[lis[1]][lis[2]] = 0
    elif lis[0] == 3 : #뒤로 이동
        for i in range(20,0,-1):
            train[lis[1]][i] = train[lis[1]][i-1]
    elif lis[0] == 4:
        for i in range(1,21): #앞으로 이동
            train[lis[1]][i] = train[lis[1]][i+1]

galaxy=set()
galaxy.add(tuple(train[1]))


for i in range(2,n+1):
    galaxy.add(tuple(train[i]))


print(len(galaxy))

    


    