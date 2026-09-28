# Task: Check for leap year
# Example Input: 2024 -> Output: Leap Year

n = 2024
print("Leap Year" if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0) else "Not Leap Year")
