# Task: Find all even numbers in a list
# Example Input: [1, 2, 3, 4, 5, 6] -> Output: [2, 4, 6]

nums = [1, 2, 3, 4, 5, 6]
print([x for x in nums if x % 2 == 0])
