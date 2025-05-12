#input
s=input()
if len(s)==1:
    if ord(s[0]) < 97:
        res = chr(ord(s[0]) + 32)
    else:
        res=chr(ord(s[0]) & ~32)
    print(res)
else:
    # dont change
    as_it_is=-1
    res=''
    for y in range(len(s)):
        if y==0:
            if ord(s[y])<97:
                res += chr(ord(s[0]) + 32)
            else:
                res += chr(ord(s[0]) & ~32)

        else:
            if ord(s[y]) >= 97:
                as_it_is+=1
                break
            else:
                res += chr(ord(s[y]) + 32)
    if as_it_is==0:
        print(s)
    else:
        print(res)
# print(ord('a'))
