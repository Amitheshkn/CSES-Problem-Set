n=int(input())
lis=[int(i) for i in input().split()]
ans=0
lis.sort()
mid = lis[len(lis)//2]
for i in range(len(lis)):
    ans+=abs(lis[i]-mid)
print(ans)