def print_right_triangle(height):
    for i in range(1, height + 1):
        for j in range(i):
            print("*", end="")
        print()

try:
    height = int(input("Enter the height of the triangle (number of rows): "))
    if height <= 0:
        print("Please enter a positive integer.")
    else:
        print_right_triangle(height)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
