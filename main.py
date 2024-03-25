import math

# Task 1: Function that calculates the  volume of a sphere
def calculate_sphere_volume(radius: int = 0):
    return round((4/3) * (math.pi * radius ** 3))

# Task 1 Demonstration
test_radius = [2, 4, 5, 10]
for radius in test_radius:
    print(f"For a sphere with a radius of '{radius}' the volume is: '{calculate_sphere_volume(radius)}'.")