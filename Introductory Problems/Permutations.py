n = int(input())
if 3 >= n > 1:
    print("NO SOLUTION")
    exit()
str1 = ""
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
    else:
        str1 += str(i) + " "
print(str1, end=" ")