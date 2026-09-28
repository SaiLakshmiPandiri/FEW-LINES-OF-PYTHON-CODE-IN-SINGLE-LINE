# Task: Remove duplicate elements from a list while keeping order
# Example Input: [1, 2, 2, 3, 1, 4] -> Output: [1, 2, 3, 4]

nums = [1, 2, 2, 3, 1, 4]
print(list(dict.fromkeys(nums)))
