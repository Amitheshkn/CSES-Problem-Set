n= int(input())
while(1):
    print(n,end=" ")
    if n==1:
        break
    elif n%2==0:
        n=n//2
    else:
        n=(n*3)+1