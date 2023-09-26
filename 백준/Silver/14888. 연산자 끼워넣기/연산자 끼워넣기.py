#백준 14888 연산자 끼워넣기
#n개의 수와 n-1개의 연산자가 주어졌을 때, 만들 수 있는 결과의 최대와 최소를 구하는 프로그램 
import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input()) # 숫자의 개수
num = list(map(int, input().split())) # 해당 숫자들

oper = list(map(int, input().split())) # 연산자 개수-> 순서대로 +, -, *, / 개수
op =[]


if oper[0] > 0 :
    while oper[0] :
        op.append("+")
        oper[0]-=1
if oper[1] > 0 :
    while oper[1] :
        op.append("-")
        oper[1]-=1
if oper[2] > 0 :
    while oper[2] :
        op.append("*")
        oper[2]-=1
if oper[3] > 0 :
    while oper[3] :
        op.append("/")
        oper[3]-=1

maxx = - int(1e9)
minn = int(1e9)

def solution():
    global maxx, minn
    for case in permutations(op,n-1):
        ans = num[0]
        for i in range(n-1) :
            if case[i] == '+':
                ans += num[i+1]
            elif case[i] == '-':
                ans -= num[i+1]
            elif case[i] == '*':
                ans *= num[i+1]
            else :
                if (ans < 0 and num[i+1] > 0) or (ans > 0 and num[i+1] < 0):
                    ans = -ans // num[i+1]
                    ans = -ans
                else :
                    ans //=num[i+1]
        if ans > maxx :
            maxx = ans
        if ans < minn :
            minn = ans


solution()
print(maxx)
print(minn)




