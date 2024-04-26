#백준 2831 댄스파티
import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
man = list(map(int,input().split()))
woman = list(map(int,input().split()))

man1 = [ i for i in man if i < 0 ]
man2 = [ i for i in man if i > 0 ]
woman1 = [ i for i in woman if i < 0 ]
woman2 = [ i for i in woman if i > 0 ]

man1.sort()
woman2.sort(reverse=True)

man2.sort(reverse=True)
woman1.sort()
m = 0
w = 0 
cnt = 0


while m < len(man1) and w < len(woman2) :
    # print(woman2[w],man1[m])
    if abs(man1[m]) > woman2[w] :
        cnt += 1
        m +=1
        w +=1
    else :
        w += 1

m = 0
w = 0 
while m < len(man2) and w < len(woman1) :           
    # print(woman1[w],man2[m])
    if man2[m] < abs(woman1[w]) :
        cnt += 1
        m += 1
        w += 1
    else :
        m += 1



print(cnt)     


