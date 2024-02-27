#백준 9996 한국이 그리울 땐 서버에 접속하지
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

front, back = input().split('*')

for _ in range(n):
    word = input()
    if len(word) < len(front)+len(back):
        print('NE')
        continue
    if word.startswith(front):
        word.replace(front,'')
        if word.endswith(back):
            print('DA')
            continue
    print('NE')







