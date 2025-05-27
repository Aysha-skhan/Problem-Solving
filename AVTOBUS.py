# hard-code
t=int(input())
for z in range(t):
    tyres=int(input())
    if tyres%6==0 and tyres%4==0:
        print(f'{tyres//6} {tyres//4}')
    elif (tyres<4):
        print(-1)
    elif tyres==4 or tyres==6:
        print(f'{1} {1}')
    elif tyres%4==0 and tyres%6!=0:
        minn=0
        divisors=tyres//4
        v2=divisors//3
        count_of_six=(v2*12)//6
        minn+=count_of_six
        minn+=divisors%3
        print(f'{minn} {tyres//4}')
    elif tyres%6==0 and tyres%4!=0:
        maxx = 0
        divisors = tyres // 6
        v2 = divisors // 2
        count_of_four = (v2 * 12) // 4
        maxx += count_of_four
        maxx += divisors % 2
        print(f'{tyres // 6} {maxx}')
    else:
        if (tyres%6)%2==0:
            maxx=0
            minn=0
            minn+=(tyres//6)+1
            maxx+=tyres//4
            print(f'{minn} {maxx}')
        else:
            print(-1)
