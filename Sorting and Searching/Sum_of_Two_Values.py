n, x = map(int, input().split())
lis=[int(i) for i in input().split()]

temp={}

for i in range(n):
    if lis[i]<=x:
        finder=x-lis[i]
        if finder in temp:
            print(i+1, temp[finder]+1)
            quit()
            
            
        else:
            temp[lis[i]]=i
print("IMPOSSIBLE")             
