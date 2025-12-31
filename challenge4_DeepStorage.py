#brute-force approach 
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

#Optimized approach
def kthSmallestBinarySearch(matrix, k):
    n = len(matrix)
    low, high = matrix[0][0], matrix[n - 1][n - 1]

    def countLessEqual(mid):
        count = 0
        row = n - 1
        col = 0

        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    while low < high:
        mid = (low + high) // 2
        if countLessEqual(mid) < k:
            low = mid + 1
        else:
            high = mid

    return low
n = int(input("Enter matrix size n: "))
matrix = []

print("Enter matrix rows:")
for _ in range(n):
    matrix.append(list(map(int, input().split())))

k = int(input("Enter k: "))
result = kthSmallest(matrix, k)
print(result)
