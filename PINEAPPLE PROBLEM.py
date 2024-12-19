# t,s,x=map(int,input().split())
# if x<(s+t) and x!=t:
#     print('NO')
# elif x==t or x%s==t%s or x%s==(t+1)%s:
#     print('YES')
# else:
#     print('NO')


t,s,x=map(int,input().split())
if x<(s+t) and x!=t:
    print('NO')
elif x==t or (x-t)%s==0 or (x-(t-1))%s==0:
    print('YES',x,x%s)
else:
    print('NO',x,x%s,t%s)
# 93647 7 451664565