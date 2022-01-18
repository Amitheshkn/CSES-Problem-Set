x=int(input())
values=[int(i) for i in input().split()]
values.sort()
ans=1
for i in range(x):
    if ans< values[i]:
        break
    else:
        ans+=values[i]
print(ans)