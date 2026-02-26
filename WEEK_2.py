# ✅ WEEK 2
# 1️⃣ Chocolate Distribution Problem
def chocolate_distribution(arr, m):
    if m > len(arr):
        return -1
    
    arr.sort()
    min_diff = float('inf')
    
    for i in range(len(arr) - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)
    
    return min_diff


arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
print(chocolate_distribution(arr, m))
# 2️⃣ Smallest Subarray with Sum Greater Than X
def smallest_subarray(arr, x):
    n = len(arr)
    min_length = n + 1
    curr_sum = 0
    start = 0
    
    for end in range(n):
        curr_sum += arr[end]
        
        while curr_sum > x:
            min_length = min(min_length, end - start + 1)
            curr_sum -= arr[start]
            start += 1
    
    return 0 if min_length == n + 1 else min_length


arr = [1, 4, 45, 6, 0, 19]
x = 51
print(smallest_subarray(arr, x))
# 3️⃣ Three-Way Partitioning (O(n))
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


arr = [1, 4, 3, 6, 2, 1]
a, b = 1, 3
print(three_way_partition(arr, a, b))
# 4️⃣ Minimum Swaps to Bring Elements ≤ k Together
def min_swaps(arr, k):
    count = sum(1 for num in arr if num <= k)
    bad = sum(1 for num in arr[:count] if num > k)
    
    ans = bad
    i = 0
    
    for j in range(count, len(arr)):
        if arr[i] > k:
            bad -= 1
        if arr[j] > k:
            bad += 1
        
        ans = min(ans, bad)
        i += 1
    
    return ans


arr = [2, 1, 5, 6, 3]
k = 3
print(min_swaps(arr, k))
# 5️⃣ Check if All Elements are Palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def all_palindrome(arr):
    for num in arr:
        if not is_palindrome(num):
            return False
    return True


arr = [111, 222, 333, 444, 555]
print(all_palindrome(arr))
# ✅ WEEK 2
6️⃣ Median of Array
def find_median(arr):
    arr.sort()
    n = len(arr)
    
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


arr = [90, 100, 78, 89, 67]
print(find_median(arr))
# 7️⃣ Spiral Matrix Traversal
def spiral_traversal(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiral_traversal(matrix))
# 8️⃣ Search in 2D Matrix (O(log m*n))
def search_matrix(matrix, target):
    if not matrix:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    left = 0
    right = rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // cols][mid % cols]
        
        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(search_matrix(matrix, 3))
# 9️⃣ Median in Row-wise Sorted Matrix
def matrix_median(mat):
    elements = []
    
    for row in mat:
        elements.extend(row)
    
    elements.sort()
    return elements[len(elements)//2]


mat = [[1,3,5],[2,6,9],[3,6,9]]
print(matrix_median(mat))
# 🔟 Row with Maximum 1s
def row_with_max_ones(arr):
    max_count = 0
    index = -1
    
    for i in range(len(arr)):
        count = sum(arr[i])
        if count > max_count:
            max_count = count
            index = i
    
    return index


arr = [[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]
print(row_with_max_ones(arr))