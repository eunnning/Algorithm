# 백준 1166 선물

n, l, w, h = map(int, input().split()) # n : 박스 개수, l,w,h : 가로,새로,높이

start = 0
end = max(l,w,h)


for i in range(10000) :
    mid = (start+ end) / 2
    if ((l//mid)*(w//mid)*(h//mid)) < n :
        end = mid
        
    else :
        start = mid
        
print("%.10f" %(end))
