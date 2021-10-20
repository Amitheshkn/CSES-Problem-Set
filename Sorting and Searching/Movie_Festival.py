n = int(input())
intervals = []
 
for i in range(n):
    a, b = map(int, input().split())
    intervals.append([a, b])
 
intervals.sort(key=lambda x: x[1])
 
ans = 0
end = -1
for interval in intervals:
    if interval[0] >= end:
        ans += 1
        end = interval[1]
print(ans)
 
