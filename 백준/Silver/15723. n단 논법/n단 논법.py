#백준 15723 n단 논법
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
lis = [[1e9]*(26) for _ in range(26)]
for i in range(26):
    lis[i][i] = 0

for _ in range(n):
    word1, word2 = input().split(" is ")
    word1 = ord(word1)- 97
    word2 = ord(word2)- 97
    lis[word1][word2] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            lis[i][j] = min(lis[i][j], lis[i][k]+lis[k][j])


m = int(input())
for _ in range(m):
    word1, word2 = input().split(" is ")
    word1 = ord(word1)-97
    word2 = ord(word2)-97
    if lis[word1][word2] < 1e9 :
        print('T')
    else :
        print('F')













