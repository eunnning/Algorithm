#백준 2502 떡 먹는 호랑이
import sys
input = sys.stdin.readline

d, k =map(int,input().split())


def fibonacci (day):
    if day == 1 or day == 2:
        return 1
    else :
        return fibonacci(day-1) + fibonacci(day-2)
    
x = fibonacci(d) #x의 계수
y = fibonacci(d-1) #y의 계수



for i in range(1, k):
    for j in range(1, k):
        if x * i + j * y == k :
            print(i)
            print(j+i)
            exit()
        
    



