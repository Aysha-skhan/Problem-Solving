n=int(input())
for z in range(n):
    a,b=map(int,input().split())
    if a==b:
        print('Bob')
    else:
        chk=abs(a-b)
        if chk%2==0:
            print('Bob')
        else:
            print('Alice')