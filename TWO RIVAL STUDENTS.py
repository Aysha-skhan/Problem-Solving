t=int(input())
#print(t)
for z in range(t):
    n,x,a,b=map(int,input().split())
    if a<b:
        diff1=abs(1-a)
        diff2=abs(n-b)
    else:
        diff1 = abs(1 - b)
        diff2 = abs(n - a)
    if x>=(diff1+diff2):
        print(diff1+diff2+abs(a-b))
    else:
        print(x+abs(a-b))
