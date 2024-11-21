def check(lenn,arr,strr):
    dict={}
    if len(strr)==lenn:
        for y in range(lenn):
            if arr[y] not in dict:
                if s[y] in dict.values():
                    return 'NO'
                dict[arr[y]]=s[y]
            elif arr[y] in dict:
                if s[y]!=dict[arr[y]]:
                    return 'NO'
    else:
        return 'NO'
    return 'Yes'

t=int(input())
for k in range(t):
    len_a=int(input())
    arr=list(map(int,input().split()))
    n=int(input())
    for y in range(n):
        s=input()
        print(check(len_a,arr,s))
