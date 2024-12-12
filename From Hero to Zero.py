t=int(input())
for z in range(t):
    n , k= map(int,input().split())
    count = 0
    while n != 0:
        if n % k == 0:
            n = n // k
            count += 1
        else:
            v=n%k
            n-=n%k
            count += v
    print(count)
# print(999999999999999999%1000000000000000000)