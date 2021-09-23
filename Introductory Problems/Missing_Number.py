n= int(input())
n1=list(map(int,input().split()))
sum1 = 0
sum2 = (n*(n+1))//2
for i in n1:
    sum1 = sum1 + i
print(sum2 - sum1)