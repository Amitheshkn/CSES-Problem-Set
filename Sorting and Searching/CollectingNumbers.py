x=int(input())
numbers=[(int(i)-1) for i in input().split()]
position=[0]*x
for i in range(x):
    position[numbers[i]]=i
rounds=1
for i in range(1,x):
    if position[i]<=position[i-1]:
        rounds+=1
print(rounds)