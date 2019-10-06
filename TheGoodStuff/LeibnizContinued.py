# Approximating pi with the Leibniz formula for pi.


iterations = 1000000
approximation = 0
sign = 1

for i in range(iterations):
    fraction = 1 / (1 + 2 * i)

    if sign < 0:  # Something easy and clever can probably be done with the sign alternating. I can't think of anything.
        approximation -= fraction
    else:
        approximation += fraction

    sign = -sign

    print(f"Approximation: {4 * approximation}")
