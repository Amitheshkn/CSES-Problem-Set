x=int(input())
numbers=[int(i+1) for i in range(x)]
while(len(numbers)>1):
    survivors=[]
    for i in range(len(numbers)):
        if i%2==1:
            print(numbers[i])
        else:
            survivors.append(numbers[i])
    if len(numbers)%2==0:
         numbers=survivors
    else:
        starter=survivors[-1]
        survivors.pop()
        survivors.insert(0,starter)
        numbers=survivors
print(numbers[0])