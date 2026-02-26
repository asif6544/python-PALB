# ✅ WEEK 
# 1️⃣ Reverse an Array (In-Place)
def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr


arr = [1, 4, 3, 2, 6, 5]
print(reverse_array(arr))
# 2️⃣ Find Minimum and Maximum
def find_min_max(arr):
    minimum = min(arr)
    maximum = max(arr)
    return [minimum, maximum]


arr = [1, 4, 3, 5, 8, 6]
print(find_min_max(arr))
# 3️⃣ Kth Smallest Element
def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]


arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
print(kth_smallest(arr, k))
# 4️⃣ Union of Two Arrays
def union_arrays(a, b):
    return list(set(a) | set(b))


a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(sorted(union_arrays(a, b)))
# 5️⃣ Largest Element
def largest_element(arr):
    return max(arr)


arr = [1, 8, 7, 56, 90]
print(largest_element(arr))
# ✅ WEEK 2
# 6️⃣ Rotate Array by One (Clockwise)
def rotate_by_one(arr):
    last = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last
    return arr


arr = [1, 2, 3, 4, 5]
print(rotate_by_one(arr))
# 7️⃣ Maximum Subarray Sum (Kadane’s Algorithm)
def max_subarray_sum(arr):
    max_current = max_global = arr[0]
    
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)
    
    return max_global


arr = [2, 3, -8, 7, -1, 2, 3]
print(max_subarray_sum(arr))
# 8️⃣ Search Insert Position (Binary Search)
def search_insert(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


nums = [1,3,5,6]
target = 5
print(search_insert(nums, target))
# 9️⃣ Two Sum
def two_sum(nums, target):
    num_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i


nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))
# 🔟 Minimum Number of Jumps
def min_jumps(arr):
    n = len(arr)
    
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    
    max_reach = arr[0]
    step = arr[0]
    jump = 1
    
    for i in range(1, n):
        if i == n - 1:
            return jump
        
        max_reach = max(max_reach, i + arr[i])
        step -= 1
        
        if step == 0:
            jump += 1
            
            if i >= max_reach:
                return -1
            
            step = max_reach - i
    
    return -1


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(min_jumps(arr))
