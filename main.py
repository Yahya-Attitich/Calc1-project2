import math


# Task 1: Function that calculates the  volume of a sphere
def calculate_sphere_volume(radius: int = 0):
    return round((4 / 3) * (math.pi * radius ** 3))


# Task 1 Demonstration
test_radius = [2, 4, 5, 10]
# for radius in test_radius:
    # print(f"For a sphere with a radius of '{radius}' the volume is: '{calculate_sphere_volume(radius)}'.")


# Task 6: Riemman Summation
def left_riemann_sum(f, n, start, end):
    dx = (end - start) / n
    sum = 0
    x = start
    for i in range(0, n):
        sum += (dx * f(x))
        x += dx
    return sum

def right_riemann_sum(f, n, start, end):
    dx = (end - start) / n
    sum = 0
    x = end
    for i in range(0, n):
        sum += (dx * f(x))
        x -= dx
    return sum

def midpoint_riemann_sum(f, n, start, end):
    dx = (end - start) / n
    sum = 0
    x = start
    for i in range(0, n):
        sum += (dx * f((x + (x + dx)) / 2))
        x += dx
    return sum

riemann_sums_test = [
    ["x^3 + 3x^2 + 4x - 1", 1, 4, 40, lambda x : x ** 3 + 3 * x ** 2 + 4 * x - 1],
    ["ln(x)", 5, 10, 40, lambda x : math.log(x, math.e)],
    ["sin(x)", 0, math.pi, 40, lambda x : math.sin(x)],
    ["e^x", 0, 2, 40, lambda x : math.e ** (x)]
]

for test in riemann_sums_test:
    print(f"""
    Function: {test[0]}
    Restrictions: [{min(test[1], test[2])} , {max(test[1], test[2])}],
    R[{test[3]}] : {right_riemann_sum(test[4], test[3], test[1], test[2])},
    L[{test[3]}] : {left_riemann_sum(test[4], test[3], test[1], test[2])},
    M[{test[3]}] : {midpoint_riemann_sum(test[4], test[3], test[1], test[2])},
    -------------------------""")