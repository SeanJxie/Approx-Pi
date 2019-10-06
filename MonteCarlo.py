import random as rnd

# Approximating pi using the Monte Carlo method.
# ----------------------------------------------
# The Monte Carlo method
#     - Let there be a circle of radius 1/2 within a square of side length 1 both centered at the same point.
#       For clarity, the center is (1/2, 1/2).
#
#     - Points with uniformly distributed random coordinates are placed on the open interval [0, 1].
#
#     - The quotient of the amount of points within the circle and the amount of points in total is taken and
#       and multiplied by 4. This number is the approximation of pi.


SQUARE_SIDE_LENGTH = 1
CIRCLE_RADIUS = SQUARE_SIDE_LENGTH / 2

points_in_circle = 0
total_points = 0
point_quantity = 1000000


def calculate_approx(inner, total):
    return 4 * inner / total


for _ in range(point_quantity):
    x = rnd.uniform(0, SQUARE_SIDE_LENGTH)
    y = rnd.uniform(0, SQUARE_SIDE_LENGTH)

    dist_from_center = ((CIRCLE_RADIUS - x) ** 2 + (CIRCLE_RADIUS - y) ** 2) ** 0.5

    if abs(dist_from_center) < CIRCLE_RADIUS:
        points_in_circle += 1

    total_points += 1

    print(f"Approx: {calculate_approx(inner=points_in_circle, total=total_points)}  # Points: {total_points}")
