n=int(input())
c=1
lis=[]
for i in range(n):
    a,b=map(int,input().split())
    lis.append([a,1])
    lis.append([b,-1])
lis.sort()
max_customers=0
act_customers=0
for i in range(len(lis)):
    act_customers+=lis[i][1]
    max_customers=max(act_customers,max_customers)
print(max_customers)