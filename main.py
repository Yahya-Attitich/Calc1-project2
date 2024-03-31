import math


# Task 1: Function that calculates the  volume of a sphere
def calculate_sphere_volume(radius: int = 0):
    return round((4 / 3) * (math.pi * radius ** 3))


# Task 1 Demonstration
test_radius = [2, 4, 5, 10]
# for radius in test_radius:
    # print(f"For a sphere with a radius of '{radius}' the volume is: '{calculate_sphere_volume(radius)}'.")


# Task 2 Pyramids
def pyramidVolume(base, height):
    x = base * base
    y = height / 3
    return x * y

# Task 2 Demonstration
print(pyramidVolume(4,4))
print(pyramidVolume(3,5))
print(pyramidVolume(5,2))

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
print(f"the roots of 3x^2 - 4x + 1 are {roots[0]} and {roots[1]}")

# Task 5 Newtons Method

def newton(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
         print('Found solution after',n,'iterations.')
         return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None
# Task 5 Demonstration

function1 = lambda x : 3 * (x ** 2) - (4 * x) + 1
function1dx = lambda x : (6 * x) - 4
approx = newton(function1, function1dx, 0.5, 1e-10, 10)
print (f'the zero of 3x^2 - 4x + 1 is {approx}') 
function2 = lambda x : x**2 - 15
function2dx = lambda x : 2 * x
sqrt15 = newton(function2, function2dx, 1, 1e-10, 10)
print (f"The squareroot of 15 is {sqrt15}")
function3 = lambda x : x**3 - 15
function3dx = lambda x: 3 * (x ** 2)
cubert = newton(function3, function3dx, 1, 1e-10, 10)
print (f"The cuberoot of 15 is {cubert}")

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
# <<<<<<< HEAD

for test in riemann_sums_test:
    print(f"""
    Function: {test[0]}
    Restrictions: [{min(test[1], test[2])} , {max(test[1], test[2])}],
    R[{test[3]}] : {right_riemann_sum(test[4], test[3], test[1], test[2])},
    L[{test[3]}] : {left_riemann_sum(test[4], test[3], test[1], test[2])},
    M[{test[3]}] : {midpoint_riemann_sum(test[4], test[3], test[1], test[2])},
    -------------------------""")

