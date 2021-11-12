n,x=[int(i) for i in input().split()]
y=[int(i) for i in input().split()]
i=0
ans=0
j=n-1
y.sort()
while(i<=j):
    if (y[i]+y[j]<=x):
        i+=1
        j-=1
    else:
        j-=1
    ans+=1
print(ans)


