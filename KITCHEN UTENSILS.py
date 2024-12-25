k,n=map(int,input().split())
utensils=list(map(int,input().split()))
dist=set(utensils)
dist=list(dist)
maxx=0
for y in range(len(dist)):
    if utensils.count(dist[y])>maxx:
        maxx=utensils.count(dist[y])
# print('maxx:',maxx)
factor=1
if maxx>n:
    factor=maxx//n
    if maxx%n!=0:
        factor+=1
total=factor*len(dist)*n
remaining=total-len(utensils)
print(remaining)
# print('total:', total)
# print('factor:', factor)
# print('len:', len(dist))

