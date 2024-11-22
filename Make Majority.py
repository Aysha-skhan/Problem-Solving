t=int(input())
for k in range(t):
    n=int(input())
    s=list(input())
    cnt_0=0
    cnt_1=0
    # print(s)
    if len(s)==1:
        if int(s[0])==0:
            print('No')
        else:
            print('Yes')
    else:
        for y in range(n-1):
            if int(s[y])==0 and int(s[y+1])==1 and y+1==n-1:
                cnt_0+=1
                cnt_1+=1
            elif int(s[y]) == 0 and int(s[y + 1]) == 1 and y+1!=n-1:
                cnt_0 += 1
            elif int(s[y])==0 and int(s[y+1])==0 and y+1==n-1:
                cnt_0+=1
            elif int(s[y])==1 and int(s[y+1])==0 and y+1==n-1:
                cnt_0+=1
                cnt_1+=1
            elif int(s[y]) == 1 and int(s[y + 1]) == 1 and y + 1 == n - 1:
                cnt_1 += 2
            elif int(s[y])==1:
                cnt_1+=1
        if cnt_1>cnt_0:
            # print('1: ', cnt_1, '0: ', cnt_0,'--yes')
            print('Yes')
        else:
            # print('1: ',cnt_1,'0: ',cnt_0,'--noo')
            print('No')

