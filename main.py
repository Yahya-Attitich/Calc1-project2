import math

# Task 1: Function that calculates the  volume of a sphere
def calculate_sphere_volume(radius: int = 0):
    return round((4/3) * (math.pi * radius ** 3))

# Task 1 Demonstration
test_radius = [2, 4, 5, 10]
for radius in test_radius:
    print(f"For a sphere with a radius of '{radius}' the volume is: '{calculate_sphere_volume(radius)}'.")

# Task 6: Riemman Summation
def left_riemman_sum(f, dx, start, end):
    sum = 0
    x = start
    while (x < end):
        sum += f(x)
        x += dx
    return sum * dx

# Task 6 Demonstration
test_riemann_sum = [
    ["polynomial", (lambda x : (x ** 3) + (3 * x ** 2) + (4 * x) - 1), 1, 4],
    ["ln(x)", (lambda x : math.log(x, math.e)), 5, 10],
    ["sin(x)", math.sin, 0, math.pi],
    ["e^x", (lambda x : math.e ** x), 0, 2]
]
for test in test_riemann_sum:
    print(f"For a function being '{test[0]}', from: '{test[2]} -> to: '{test[3]}', the area under the curve is: {left_riemman_sum(test[1],1, test[2], test[3])}.")