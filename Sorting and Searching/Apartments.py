n, m, k = [int(x) for x in input().split()]
applicant = [int(x) for x in input().split()]
apartment = [int(x) for x in input().split()]

applicant.sort()
apartment.sort()

ans = 0
i = 0
j = 0

while i != len(applicant) and j != len(apartment):
    if applicant[i] - k <= apartment[j] <= applicant[i] + k:
        ans += 1
        i += 1
        j += 1

    elif apartment[j] < applicant[i] - k:
        j += 1
    else:
        i += 1

print(ans)