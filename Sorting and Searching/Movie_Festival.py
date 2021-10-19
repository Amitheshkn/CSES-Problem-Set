n=int(input())
temp=[]
for i in range(n):
    x,y  = map(int,input().split())
    temp.append([y,x])
temp.sort()
ans=0
end=0
for i in range(n):
    if temp[i][1]>=end:
        ans+=1
        end=temp[i][0]
print(ans)