# 백준 1747 소수& 팰린드롬

n = int(input())

cnt = 1

N = 1003002

prime = [True] * N
m = int(N**0.5)
for i in range(2, m+1):
    if prime[i]==True:
        for j in range(i+i,N,i):
            prime[j]=False



def palindrome(i):
    p = str(i) 
    if p == p[::-1] :
        return True
    else :
        return False

             
            
for i in range(3,N):
    if n == 1 or n == 2:
        print(2)
        break
    
    if prime[i]==True :
        if palindrome(i) :
            if i >= n :
                print(i)
                break


    