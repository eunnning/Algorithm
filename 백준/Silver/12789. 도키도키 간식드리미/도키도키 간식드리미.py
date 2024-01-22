#백준 12789 도키도키 간식드리미
import sys
input = sys.stdin.readline

n = int(input())

lis = list(map(int, input().split()))

stack =[]

start = 1

for i in range(n):
    tmp = lis.pop(0)
    if start == tmp :
        start +=1
    else :
        while len(stack) != 0 :
            if stack[-1] == start :
                stack.pop()
                start +=1
            else :
                break
        stack.append(tmp)

m = len(stack)

for i in range(m):
    tmp = stack.pop()
    if start == tmp:
        start += 1
    else :
        print('Sad')
        exit()

print('Nice')
