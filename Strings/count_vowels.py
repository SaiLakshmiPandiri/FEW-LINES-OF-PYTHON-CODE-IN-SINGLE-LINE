# Task: Count the number of vowels in a string
# Example Input: "coding muchatlu" -> Output: 5

s = "coding muchatlu"
print(sum(c.lower() in "aeiou" for c in s))
