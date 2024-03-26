import math

# Task 1: Function that calculates the  volume of a sphere
def calculate_sphere_volume(radius: int = 0):
    return round((4/3) * (math.pi * radius ** 3))

# Task 1 Demonstration
test_radius = [2, 4, 5, 10]
for radius in test_radius:
    print(f"For a sphere with a radius of '{radius}' the volume is: '{calculate_sphere_volume(radius)}'.")

# Task 3 Derivatives!
def derivative(f, x):
    h = 1e-6
    return round(((f(x+h) - f(x))/h), 5)

# Task 3 Demonstration
x = 1
test_derivative = derivative((lambda x : 3 * x**2 - (6 * x) + 1), x)
print(f"The slope of (3x)^2 - 6x + 1 at x = {x} is {test_derivative}")

# Task 4 quadratic formula
def quadratic(a, b, c):
    numerator = b**2 - 4 * a * c 
    if numerator < 0:
        return []
    elif numerator == 0:
        root = -b / (2 * a)
        return [root]
    else:
        root1 = (-b + math.sqrt(numerator)) / (2 * a)
        root2 = (-b - math.sqrt(numerator)) / (2 * a)
        return [root1, root2]
    
# Task 4 Demonstration
roots = quadratic(3, -4, 1)
print(f"the roots of 3x^2 -4x + 1 are {roots[0]} and {roots[1]}")

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
