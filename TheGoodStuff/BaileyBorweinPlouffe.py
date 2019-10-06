# Approximating Pi using the  Bailey–Borwein–Plouffe formula.
# This is an extremely quick converging series. The precision goes beyond Python's float number.

iterations = 1000000
approximation = 0

for k in range(iterations):
    approximation += (1 / 16 ** k) * ((4 / (8 * k + 1)) - (2 / (8 * k + 4)) - (1 / (8 * k + 5)) - (1 / (8 * k + 6)))
    print(approximation)

