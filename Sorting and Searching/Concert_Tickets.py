n,m=[int(i) for i in input().split()]
tickets=[int(i) for i in input().split()]
price=[int(i) for i in input().split()]
tickets.sort(reverse=True)
for i in price:
    ans=0
    set=False
    for j in range(len(tickets)):
        if i>=tickets[j]:
            set=True
            print(tickets[j])
            tickets.remove(tickets[j])
            break
    if set==False:
        print("-1")

