# 🐍 FEW LINES OF PYTHON CODE IN SINGLE LINE

Welcome to **Coding Muchatlu's** official collection of Python one-liners, tips, and tricks! 🚀  
This repository contains clean, concise, and efficient single-line Python solutions to everyday programming tasks and interview problems.

---

## 📌 One-Liner Index

| # | Topic | Category | One-Liner Snippet | Code Link |
|---|---|---|---|---|
| 01 | Sum of Numbers | Basics | `print(sum(nums))` | [01_sum_of_numbers.py](./Basics/01_sum_of_numbers.py) |
| 02 | Factorial | Basics | `import math; print(math.factorial(n))` | [02_factorial.py](./Basics/02_factorial.py) |
| 03 | Square of a Number | Basics | `print(n ** 2)` | [03_square_of_a_number.py](./Basics/03_square_of_a_number.py) |
| 04 | Cube of a Number | Basics | `print(n ** 3)` | [04_cube_of_a_number.py](./Basics/04_cube_of_a_number.py) |
| 05 | Leap Year Check | Conditions | `print("Leap Year" if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0) else "Not Leap Year")` | [05_leap_year_check.py](./Conditions_and_Logic/05_leap_year_check.py) |
| 06 | Count Vowels | Strings | `print(sum(c.lower() in "aeiou" for c in s))` | [06_count_vowels.py](./Strings/06_count_vowels.py) |
| 14 | Remove Duplicates | Lists | `print(list(dict.fromkeys(nums)))` | [14_remove_duplicates.py](./Lists_and_Arrays/14_remove_duplicates.py) |
| 15 | Sort a List | Lists | `print(sorted(nums))` | [15_sort_a_list.py](./Lists_and_Arrays/15_sort_a_list.py) |
| 16 | Find Even Numbers | Lists | `print([x for x in nums if x % 2 == 0])` | [16_find_even_numbers.py](./Lists_and_Arrays/16_find_even_numbers.py) |
| 17 | Find Odd Numbers | Lists | `print([x for x in nums if x % 2 != 0])` | [17_find_odd_numbers.py](./Lists_and_Arrays/17_find_odd_numbers.py) |
| 18 | Sum of Digits | Basics | `print(sum(map(int, str(n))))` | [18_sum_of_digits.py](./Basics/18_sum_of_digits.py) |
| 19 | Multiplication Table | Basics | `print(*[n * i for i in range(1, 11)])` | [19_multiplication_table.py](./Basics/19_multiplication_table.py) |
| 20 | Fibonacci Series | Algorithms | `print((lambda f: [f.append(f[-1]+f[-2]) for _ in range(n-2)] and f)([0,1]))` | [20_fibonacci_series.py](./Algorithms/20_fibonacci_series.py) |

---

## 🛠️ How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/SaiLakshmiPandiri/FEW-LINES-OF-PYTHON-CODE-IN-SINGLE-LINE.git](https://github.com/SaiLakshmiPandiri/FEW-LINES-OF-PYTHON-CODE-IN-SINGLE-LINE.git)
