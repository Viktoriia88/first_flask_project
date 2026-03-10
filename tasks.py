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
    best = 1
    cur = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            cur += 1
        else:
            cur = 1
        best = max(best, cur)

    return best

#Diff two lists
# expected = ["login", "logout", "settings"]
# actual   = ["login", "profile"]
# Задача вывести что есть в expected, но нет в actual; что есть в actual, но нет в expected; что есть в обоих; обьединение двух массивов
# missing     -> ["logout", "settings"]
# unexpected  -> ["profile"]
# common      -> ["login"]

def diff_lists(expected, actual):
    expected = set(expected)
    actual = set(actual)

    missing = list(expected.difference(actual))
    unexpected = list(actual.difference(expected))
    common = list(expected.intersection(actual))
    all = list(expected.union(actual))

    return missing, unexpected, common, all

#  Diff two lists with duplicates (такая же как предидущая только учитывает дубликаты)
from collections import Counter

def diff_lists_multiset(expected, actual):
    ce = Counter(expected)
    ca = Counter(actual)

    missing = list((ce - ca).elements())

    unexpected = list((ca - ce).elements())

    common = list((ca & ce).elements())

    return missing, unexpected, common

# Valid Parentheses
# "()" -> True
# "[(])" -> True
# "([)]" -> False
def is_valid(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}

    stack = []

    for c in s:
        if c in pairs.values():
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False


    return not stack

# Two Sum
# Задача состоит в том что нужно найти пару которая дает в сумме значение target
# nums = [3, 2, 4],  target = 6  -> (1, 2)
def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return seen[need], i

        seen[num] = i

# Remove Duplicates (sorted, in-place)
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    def remove_duplicates(nums):

        slow = 0

        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1

# Remove Duplicates II
# Нужно модифицировать массив in-place так, чтобы каждый элемент встречался не больше 2 раз, и вернуть новую длину k.
# nums = [0,0,0,0,1,1,1,1,2,3,3] ->  [0,0,1,1,2,3,3]  Ответ будет k = 7
def remove_duplicates_two(nums):
    slow = 2

    for fast in range(2, len(nums)):

        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1

    return slow

# Merge Sorted Arrays
# arrays is sorted
# a = [1, 3, 5]  and b = [2, 4, 6] -> [1, 2, 3, 4, 5, 6]
def merge_sorted(a, b):
    i = 0
    j = 0
    res = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    # дописываем хвост
    res.extend(a[i:])
    res.extend(b[j:])

    return res

# Parse query string
# qs = "a=1&b=2&c=hello%20world&b=3&b=7&empty=&flag"
# {
#   "a": "1",
#   "b": ["2", "3"],
#   "c": "hello world",
#   "empty": "",
#   "flag": "true"
# }
def parse_qs(qs: str) -> dict:
    result = {}

    for q in qs.split('&'):
        if '=' in q:
            key, value = q.split('=', 1)
            value = value.replace("%20", ' ')
        else:
            key, value = q, "true"

        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value

    return dict(result)

# List[dict] processing
# tests = [
#   {"suite": "smoke", "name": "login", "status": "pass"},
#   {"suite": "smoke", "name": "logout", "status": "fail"},
#   {"suite": "regression", "name": "profile", "status": "pass"},
#   {"suite": "smoke", "name": "settings", "status": "pass"},
#   {"suite": "regression", "name": "billing", "status": "skip"},
# ]
# {
#   "smoke": {
#     "pass": 2, "fail": 1, "skip": 0,
#     "failed_tests": ["logout"]
#   },
#   "regression": {
#     "pass": 1, "fail": 0, "skip": 1,
#     "failed_tests": []
#   }
# }
def summarize_tests(tests):

    res = {}

    for item in tests:
        suite = item['suite']
        status = item['status']
        name = item['name']
        if suite not in res:
            res[suite] = {'pass': 0, 'fail': 0, 'skip': 0, 'failed_tests': []}

        res[suite][status] += 1

        if status == 'fail':
            res[suite]['failed_tests'].append(name)


    return res


