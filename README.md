# 🐍 FEW LINES OF PYTHON CODE IN SINGLE LINE

Welcome to **Coding Muchatlu's** official collection of Python one-liners, tips, and tricks! 🚀  
This repository contains clean, concise, and efficient single-line Python solutions to everyday programming tasks and interview problems.

---

## 📌 One-Liner Index

| # | Topic | Category | One-Liner Snippet | Code Link |
|---|---|---|---|---|
| 01 | Sum of Numbers | Basics | `print(sum(nums))` | [sum_of_numbers.py](./Basics/sum_of_numbers.py) |
| 02 | Factorial | Basics | `import math; print(math.factorial(n))` | [factorial.py](./Basics/factorial.py) |
| 03 | Square of a Number | Basics | `print(n ** 2)` | [square_of_a_number.py](./Basics/square_of_a_number.py) |
| 04 | Cube of a Number | Basics | `print(n ** 3)` | [cube_of_a_number.py](./Basics/cube_of_a_number.py) |
| 05 | Sum of Digits | Basics | `print(sum(map(int, str(n))))` | [sum_of_digits.py](./Basics/sum_of_digits.py) |
| 06 | Multiplication Table | Basics | `print(*[n * i for i in range(1, 11)])` | [multiplication_table.py](./Basics/multiplication_table.py) |
| 07 | Leap Year Check | Conditions | `print("Leap Year" if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0) else "Not Leap Year")` | [leap_year_check.py](./Conditions_and_Logic/leap_year_check.py) |
| 08 | Even or Odd | Conditions | `print("Even" if n % 2 == 0 else "Odd")` | [even_or_odd.py](./Conditions_and_Logic/even_or_odd.py) |
| 09 | Positive or Negative | Conditions | `print("Positive" if n > 0 else "Negative" if n < 0 else "Zero")` | [positive_or_negative.py](./Conditions_and_Logic/positive_or_negative.py) |
| 10 | Largest of Two | Conditions | `print(max(a, b))` | [largest_of_two.py](./Conditions_and_Logic/largest_of_two.py) |
| 11 | Largest of Three | Conditions | `print(max(a, b, c))` | [largest_of_three.py](./Conditions_and_Logic/largest_of_three.py) |
| 12 | Smallest of Three | Conditions | `print(min(a, b, c))` | [smallest_of_three.py](./Conditions_and_Logic/smallest_of_three.py) |
| 13 | Count Vowels | Strings | `print(sum(c.lower() in "aeiou" for c in s))` | [count_vowels.py](./Strings/count_vowels.py) |
| 14 | Palindrome Check | Strings | `print("Palindrome" if s == s[::-1] else "Not Palindrome")` | [palindrome_check.py](./Strings/Palindrome_Check.py) |
| 15 | Reverse a String | Strings | `print(s[::-1])` | [reverse_string.py](./Strings/reverse_string.py) |
| 16 | Remove Duplicates | Lists | `print(list(dict.fromkeys(nums)))` | [remove_duplicates.py](./Lists_and_Arrays/remove_duplicates.py) |
| 17 | Sort a List | Lists | `print(sorted(nums))` | [sort_a_list.py](./Lists_and_Arrays/sort_a_list.py) |
| 18 | Find Even Numbers | Lists | `print([x for x in nums if x % 2 == 0])` | [find_even_numbers.py](./Lists_and_Arrays/find_even_numbers.py) |
| 19 | Find Odd Numbers | Lists | `print([x for x in nums if x % 2 != 0])` | [find_odd_numbers.py](./Lists_and_Arrays/find_odd_numbers.py) |
| 20 | Fibonacci Series | Algorithms | `print((lambda f: [f.append(f[-1]+f[-2]) for _ in range(n-2)] and f)([0,1]))` | [fibonacci_series.py](./Algorithms/fibonacci_series.py) |

---

## 🛠️ How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/SaiLakshmiPandiri/FEW-LINES-OF-PYTHON-CODE-IN-SINGLE-LINE.git](https://github.com/SaiLakshmiPandiri/FEW-LINES-OF-PYTHON-CODE-IN-SINGLE-LINE.git)
