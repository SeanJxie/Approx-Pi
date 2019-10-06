# Using the mildly complex but rapidly converging Ramanjunan series for approximating Pi.
# The formula can be found at https://en.wikipedia.org/wiki/Approximations_of_%CF%80.

iterations = 1000000
approximation = 0


def factorial(n):
    res = 1
    for i in range(n):
        res *= n - i
    return res


multiplier1 = (2 * 2 ** 0.5) / 9801
multiplier2 = 0
for k in range(iterations):  # The approximation gets a little too precise.
    multiplier2 += (factorial(4 * k) * (1103 + 26390 * k)) / (factorial(k) ** 4 * 394 ** (4 * k))
    print(f"Approximation: {1 / (multiplier1 * multiplier2)}")
