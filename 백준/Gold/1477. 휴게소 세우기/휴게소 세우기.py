#백준 1477 휴게소 세우기

import sys
input = sys.stdin.readline

n, m, l = map(int,input().split())

rest_area = [0]+list(map(int, input().split()))+[l]

rest_area.sort()

distance = []
for i in range(len(rest_area)-1):
    distance.append(rest_area[i+1]-rest_area[i])

start = 1
end = l-1

while start <= end :
    mid = (start + end) // 2
    if mid == 0 :
        print(1)
        exit()
    count = 0 
    for i in distance :
        count += (i-1) // mid
    if count <= m :
        end = mid - 1
    else :
        start = mid + 1


print(start)


