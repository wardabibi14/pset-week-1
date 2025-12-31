def kthSmallest(matrix, k):
    arr = []
    for row in matrix:
        for val in row:
            arr.append(val)

    arr.sort()
    return arr[k - 1]
n = int(input("Enter matrix size n: "))
matrix = []

print("Enter matrix rows:")
for _ in range(n):
    matrix.append(list(map(int, input().split())))

k = int(input("Enter k: "))
result = kthSmallest(matrix, k)
print(result)