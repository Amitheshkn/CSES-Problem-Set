x=input()
count=0
while(1):
    if len(x)==1:
        count+=1
        break
    temp=sorted(x)[-1]
    x=str(int(x)-int(temp))
    count+=1
print(count) 
