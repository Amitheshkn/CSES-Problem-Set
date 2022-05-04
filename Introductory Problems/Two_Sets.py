n = int(input())
elements = list(range(1, n + 1))
sum_of_elements = (n * (n + 1)) // 2
if sum_of_elements % 2 == 1:
    print("NO")
else:
    print("YES")
    set2 = []
    target = sum_of_elements // 2
    while target > elements[-1]:
        x = elements.pop()
        target -= x
        set2.append(x)
    elements.remove(target)
    set2.append(target)
    print(len(elements))
    print(*elements)
    print(len(set2))
    print(*set2)
