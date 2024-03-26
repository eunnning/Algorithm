#백준 31433 KSA문자열
import sys
input = lambda: sys.stdin.readline().rstrip()

word = input()
n = len(word)
KSA = ['K','S','A']
cnt = 0
ans = 1e9
def sol(str, cnt):
    global ans
    string = ''
    m = len(str) 
    for i in range(m):
        if str[i] == 'K' and len(string) % 3 == 0:
            string += str[i]
        elif str[i] == 'S' and len(string) % 3 == 1:
            string += str[i]
        elif str[i] == 'A' and len(string) % 3 == 2 :
            string += str[i]
        else :
            cnt += 1
    cnt += abs(len(string)-n)
    ans = min(cnt, ans)

sol(word,0)
sol('K'+word,1)
sol('KS'+word,2)
print(ans)






