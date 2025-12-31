#brute-force approach
def findMedian(scoresA, scoresB):
    merged = []
    i = j = 0

    while i < len(scoresA) and j < len(scoresB):
        if scoresA[i] < scoresB[j]:
            merged.append(scoresA[i])
            i += 1
        else:
            merged.append(scoresB[j])
            j += 1

    while i < len(scoresA):
        merged.append(scoresA[i])
        i += 1

    while j < len(scoresB):
        merged.append(scoresB[j])
        j += 1

    n = len(merged)
    if n % 2 == 1:
        return float(merged[n // 2])
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2

scoresA = list(map(int, input("Enter scoresA: ").split()))
scoresB = list(map(int, input("Enter scoresB: ").split()))
result = findMedian(scoresA, scoresB)
print(result)


#Optimized approach
def BalancedScore(scoresA, scoresB):
    m, n = len(scoresA), len(scoresB)
    total = m + n

    i = j = 0
    prev = curr = 0

    for count in range(total // 2 + 1):
        prev = curr

        if i < m and (j >= n or scoresA[i] <= scoresB[j]):
            curr = scoresA[i]
            i += 1
        else:
            curr = scoresB[j]
            j += 1

    if total % 2 == 1:
        return float(curr)
    else:
        return (prev + curr) / 2

scoresA = list(map(int, input("Enter scoresA: ").split()))
scoresB = list(map(int, input("Enter scoresB: ").split()))
result = BalancedScore(scoresA, scoresB)
print(result)