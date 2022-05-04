n = int(input())
x = list(map(int, input().split()))
mx = -1
output = 0
for i in range(n):
    if x[i] < mx:
        output += mx - x[i]
    mx = max(mx, x[i])
print(output)
