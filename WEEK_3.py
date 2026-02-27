# 1️⃣ Chocolate Distribution Problem
def chocolate_distribution(arr, m):
    n = len(arr)
    if m == 0 or n == 0 or m > n:
        return 0

    arr.sort()
    min_diff = float('inf')

    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)

    return min_diff


# Example
print(chocolate_distribution([3,4,1,9,56,7,9,12], 5))
# 2️⃣ Smallest Subarray with Sum Greater Than X
def smallest_subarray(x, arr):
    n = len(arr)
    min_len = n + 1
    curr_sum = 0
    start = 0

    for end in range(n):
        curr_sum += arr[end]

        while curr_sum > x:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    return 0 if min_len == n + 1 else min_len


print(smallest_subarray(51, [1,4,45,6,0,19]))
# 3️⃣ Three Way Partitioning (O(n))
def three_way_partition(arr, a, b):
    start = 0
    end = len(arr) - 1
    i = 0

    while i <= end:
        if arr[i] < a:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1
        elif arr[i] > b:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1
    return arr


print(three_way_partition([1,4,3,6,2,1], 1, 3))
# 4️⃣ Minimum Swaps to Bring ≤ k Together
def min_swaps(arr, k):
    count = sum(1 for num in arr if num <= k)

    bad = sum(1 for num in arr[:count] if num > k)
    ans = bad

    for i in range(len(arr) - count):
        if arr[i] > k:
            bad -= 1
        if arr[i + count] > k:
            bad += 1
        ans = min(ans, bad)

    return ans


print(min_swaps([2,1,5,6,3], 3))
# 5️⃣ All Elements Palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def all_palindrome(arr):
    for num in arr:
        if not is_palindrome(num):
            return False
    return True


print(all_palindrome([111,222,333,444,555]))

# 6️⃣ Find Median of Array
def find_median(arr):
    arr.sort()
    n = len(arr)

    if n % 2 == 1:
        return arr[n//2]
    else:
        return (arr[n//2 - 1] + arr[n//2]) / 2


print(find_median([90,100,78,89,67]))
# 7️⃣ Spiral Traversal of Matrix
def spiral_traversal(matrix):
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1

    while top <= bottom and left <= right:
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


print(spiral_traversal([[1,2,3],[4,5,6],[7,8,9]]))
# 8️⃣ Search in 2D Matrix (Binary Search O(log m*n))
def search_matrix(matrix, target):
    if not matrix:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m*n - 1

    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // n][mid % n]

        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(search_matrix([[1,3,5],[7,9,11]], 9))
# 9️⃣ Median in Row-wise Sorted Matrix
import bisect

def matrix_median(matrix):
    r = len(matrix)
    c = len(matrix[0])

    min_val = min(row[0] for row in matrix)
    max_val = max(row[-1] for row in matrix)

    desired = (r * c + 1) // 2

    while min_val < max_val:
        mid = (min_val + max_val) // 2
        count = 0

        for row in matrix:
            count += bisect.bisect_right(row, mid)

        if count < desired:
            min_val = mid + 1
        else:
            max_val = mid

    return min_val


print(matrix_median([[1,3,5],[2,6,9],[3,6,9]]))
# 🔟 Row with Maximum 1s
def row_with_max_1s(matrix):
    max_count = 0
    index = -1

    for i in range(len(matrix)):
        count = sum(matrix[i])
        if count > max_count:
            max_count = count
            index = i

    return index


print(row_with_max_1s([[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]))