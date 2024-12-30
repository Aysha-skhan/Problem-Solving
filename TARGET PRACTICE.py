def points(v):
    points=0
    if (v<=9) or (v%10==0 or v%10==9) or (v>89 and v<100):
        points+=1
    elif (v>10 and v<19) or (v%10==1 or v%10==8)or (v>80 and v<89):
        points+=2
    elif (v>21 and v<28) or (v%10==2 or v%10==7)or (v>71 and v<78):
        points+=3
    elif (v>32 and v<37) or (v%10==3 or v%10==6)or (v>62 and v<67):
        points+=4
    elif v==54 or v==55 or v==44 or v==45:
        points+=5
    return points

t=int(input())
for z in range(t):
    original = ''
    final_points=0
    for y in range(10):
        s=input()
        original+=s
    # print(original)
    for t in range(len(original)):
        if original[t]=='X':
            # print(t)
            # print(original[t])
            final_points+=points(t)
            # print('points:', points(t),'line: ',t)
    print(final_points)
