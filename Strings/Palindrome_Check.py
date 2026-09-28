# Task: Check if a string is a palindrome
# Example Input: "radar" -> Output: True

s = "radar"
print("Palindrome" if s == s[::-1] else "Not Palindrome")
