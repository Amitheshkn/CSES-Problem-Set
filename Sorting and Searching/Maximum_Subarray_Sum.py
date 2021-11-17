x=int(input())
values=[int(i) for i in input().split()]
past=0
best=-1e18
for i in range(x):
    if past+values[i]>=values[i]:
        past+=values[i]
    else:
        past=values[i]
    best=max(past,best)
print(best)