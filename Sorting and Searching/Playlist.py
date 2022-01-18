n=int(input())
lis=[int(i) for i in input().split()]
temp=set()
count=0
j=0
for i in range(n):
    while lis[i] in temp:
        temp.remove(lis[j])
        j+=1
    temp.add(lis[i])
    count=max(count,len(temp))
print(count)