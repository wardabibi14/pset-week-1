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
