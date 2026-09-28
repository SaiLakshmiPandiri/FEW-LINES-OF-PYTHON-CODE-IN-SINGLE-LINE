# Task: Generate the Fibonacci series of the first n terms
# Example Input: 7 -> Output: [0, 1, 1, 2, 3, 5, 8]

n = 7
print((lambda f: [f.append(f[-1] + f[-2]) for _ in range(n - 2)] and f)([0, 1]))
