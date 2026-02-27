# 1️⃣ Search Insert Position (O(log n))
def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
# 2️⃣ Combination Sum (Unlimited Use)
def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()
    
    backtrack(0, [], 0)
    return result
# 3️⃣ Combination Sum II (Single Use)
def combination_sum2(candidates, target):
    candidates.sort()
    result = []
    
    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()
    
    backtrack(0, [], 0)
    return result
# 4️⃣ Jump Game II (Greedy O(n))
def jump(nums):
    jumps = 0
    farthest = 0
    end = 0
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == end:
            jumps += 1
            end = farthest
    
    return jumps
# 5️⃣ Group Anagrams
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    
    return list(anagrams.values())
# 6️⃣ Plus One
def plus_one(digits):
    n = len(digits)
    
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    return [1] + digits
# 7️⃣ Set Matrix Zeroes (In-place)
def set_zeroes(matrix):
    rows = set()
    cols = set()
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in cols:
                matrix[i][j] = 0
    
    return matrix
# ✅ WEEK 2
# 8️⃣ Search in 2D Matrix (O(log m*n))
def search_matrix(matrix, target):
    if not matrix:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
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
# 9️⃣ Sort Colors (Dutch National Flag – O(n))
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    
    return nums
# 🔟 Subsets (Power Set)
def subsets(nums):
    result = [[]]
    
    for num in nums:
        result += [curr + [num] for curr in result]
    
    return result
# 1️⃣1️⃣ Word Search (Backtracking)
def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
            return False
        
        temp = board[r][c]
        board[r][c] = "#"
        
        found = (dfs(r+1, c, index+1) or
                 dfs(r-1, c, index+1) or
                 dfs(r, c+1, index+1) or
                 dfs(r, c-1, index+1))
        
        board[r][c] = temp
        return found
    
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    
    return False
# 1️⃣2️⃣ 4Sum
def four_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            left, right = j + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif total < target:
                    left += 1
                else:
                    right -= 1
    
    return result
# 1️⃣3️⃣ Search in Rotated Sorted Array (O(log n))
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
# 1️⃣4️⃣ Find First and Last Position (O(log n))
def search_range(nums, target):
    
    def find_left():
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            if nums[mid] == target:
                index = mid
        return index
    
    def find_right():
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] == target:
                index = mid
        return index
    
    return [find_left(), find_right()]