# Task: Print the multiplication table (1 to 10)
# Example Input: 5 -> Output: 5 10 15 20 25 30 35 40 45 50

n = 5
print(*[n * i for i in range(1, 11)])
