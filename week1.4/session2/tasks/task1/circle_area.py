# Week 4, Session 2: Task 1

# Define a function circle_area with an optional pi_value argument
def circle_area(radius, pi_value=3.14):
    # Calculate the area of the circle
    area = pi_value * radius ** 2

    return area


# Check if correct output is produced
print(circle_area(2))
print(circle_area(5))
print(circle_area(22.5))
