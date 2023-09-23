# 백준 1074 Z

n, r, c = map(int, input().split())

ans = 0

def Z (m, a, b) :
    global ans
    if m != 0 :
        m -= 1
        if a < 2**m and b < 2**m : # 1사분면
            ans += (2**m)*(2**m)*0
        
        if a < 2**m and b >= 2**m : # 2사분면
            ans += (2**m)*(2**m)
            b -=(2**m)
        
        if a >= 2**m and b < 2**m : #3사분면
            ans += (2**m)*(2**m)*2
            a -=(2**m) 
        
        if a >= 2**m and b >= 2**m : # 4사분면
            ans += (2**m)*(2**m)*3 
            a -=(2**m) 
            b -=(2**m)
            
        
          
        
        Z(m,a,b)
 
        
    
Z(n,r,c)        
    
print(ans)