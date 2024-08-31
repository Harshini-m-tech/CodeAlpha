def calculate_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

# User input for radius
radius = int(input("Enter the radius of the circle: "))

# Convert input to float
radius_float = float(radius)

# Calculate area
area = calculate_area(radius_float)

print("The area of the circle is: " + area)