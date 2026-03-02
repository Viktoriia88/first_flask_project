arr = [1, 2, 3, 4, 5] #-> [2, 4, 1, 3, 5]
# [2, 4, 6] -> [2, 4, 6]
# [1, 3, 5] -> [1, 3, 5]
# [] -> []
def stable_even_first(nums):
    res = []

    for num in nums:
        if num % 2 == 0:
            res.append(num)

    for num in nums:
        if num % 2 != 0:
            res.append(num)

    return res

print(stable_even_first(arr))