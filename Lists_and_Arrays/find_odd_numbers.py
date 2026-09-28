# Task: Find all odd numbers in a list
# Example Input: [1, 2, 3, 4, 5] -> Output: [1, 3, 5]

nums = [1, 2, 3, 4, 5]
print([x for x in nums if x % 2 != 0])
