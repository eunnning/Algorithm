#백준 18114 블랙프라이데이
import sys
input = sys.stdin.readline

n, c = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()

start = 0
end = n-1

# 1개 선택
while start <= end :
    mid = (start + end) // 2
    if lis[mid] > c :
        end = mid - 1
    elif lis[mid] == c :
        print(1)
        exit()
    else :
        start = mid + 1

for i in range(n):
    start = i+1
    end = n-1
    summ = lis[i]
    while start <= end :
        mid = (start + end) // 2
        if summ + lis[mid] > c :
            end = mid - 1
        elif summ + lis[mid] == c :
            print(1)
            exit()
        else :
            start = mid + 1

for i in range(n):
    for j in range(i+1, n):
        if lis[i] + lis[j] < c :
            tmp = c - lis[i] - lis[j]
            start = j + 1
            end = n -1
            while start<= end :    
                mid = (start + end) // 2
                if lis[mid] > tmp :
                    end = mid - 1
                elif lis[mid] == tmp :
                    print(1)
                    exit()
                else :
                    start = mid + 1

print(0)
        
