n=int(input())
s=list(input())
part1=s[:n]
part2=s[n:]
flag=-1
wrong=0
part1.sort()
part2.sort()
for k in range(n):
    if part1[k]<part2[k]:
        if flag==1:
            wrong+=1
            break
        elif flag==-1:
            flag=0
    elif part1[k]>part2[k]:
        if flag==-1:
            flag=1
        elif flag==0:
            wrong+=1
            break
    else:
        wrong+=1
        break
if wrong==0:
    print('YES')
else:
    print('NO')
