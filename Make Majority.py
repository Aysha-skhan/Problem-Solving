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


# s='aysha'
# t=list(s)
# print(t)
# # s=s[2:]
# t=s[2:]
# print(t)
# 100001100

# 1
# 1
# 6
# 101000
# 1
# 1
# 4
# 0001
# 3
# 000
# 1
# 0
# 2
# 00
# 1
# 1
# 6
# 001100
# 8
# 10001101
# 1
# 1
# 1
# 0
# 1
# 0
# 8
# 00011110
# 7
# 0110100
# 1
# 0
# 8
# 01111011
# 8
# 10100011
# 1
# 0
# 8
# 01000101
# 6
# 010100
# 4
# 0101
# 4
# 1111
# 5
# 10100
# 7
# 1000010
# 6
# 110010
# 3
# 011
# 5
# 11101
# 5
# 10101
# 2
# 11
# 4
# 1000
# 6
# 010111
# 4
# 0001
# 6
# 100000
# 2
# 10
# 2
# 01
# 7
# 1110010
# 7
# 1000011
# 4
# 0101
# 1
# 0
# 6
# 001000
# 5
# 11100
# 5
# 00100
# 2
# 11
# 5
# 11000
# 5
# 10101
# 2
# 10
# 4
# 1111
# 2
# 10
# 8
# 11011100
# 8
# 10000111
# 7
# 0001001
# 2
# 11