n = input()
n = [i for i in n]
count = 0
maxcount = 0
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        count += 1
        if count >= maxcount:
            maxcount = count

    else:
        count = 0
print(maxcount + 1)