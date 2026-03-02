# Rotate array
# [1,2,3,4,5], k=2 → [4,5,1,2,3]

def rotate(nums, k):
    if not nums:
        return nums
    k %= len(nums)
    return nums[-k:] + nums[:-k]


# Remove duplicates
# [1, 2, 2, 3, 1] -> [1, 2, 3]

def dedup_stable(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

 # Move Zeroes to the end
 # [3, 1, 0, 3, 0] -> [3, 1, 3, 0, 0]

def move_zeroes(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    return nums

# Chunking
# arr = [1, 2, 3, 4, 5], size = 2 -> результат: [[1, 2], [3, 4], [5]]

def chunk(arr, size):
    result = []
    if not size:
        return []

    start = 0
    stop = size

    while start < len(arr):
        result.append(arr[start:stop])
        start += size
        stop += size

    return result

# Longest Increasing Run
# [1, 2, 3, 2, 3, 4, 5, 1] -> 4   # (2,3,4,5)

def longest_increasing_run(nums):
    if not nums:
        return 0

    best = 1
    cur = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            cur += 1
        else:
            cur = 1
        best = max(best, cur)

    return best