#inp
t=int(input())
#loop
for y in range(t):
    n,m=map(int,input().split())
    cells=n*m
    blue=cells//3
    rem=cells%3
    # rem
    if rem > 0:
        blue+=1
    print(blue)
