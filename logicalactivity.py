# Ask the user to input their age
age = int(input("Enter your age: "))

# Ask the user to input whether they are a student or not
student = input("Are you a student? (yes/no): ")

# Use logical operators to determine if the person is eligible for a discount
# If the person is 12 years old or younger, they get a discount
# If the person is between 13 and 18 years old (inclusive) and they are a student, they get a discount
discount = (age <= 12) or (13 <= age <= 18 and student == "yes")

# Print a message indicating whether the person is eligible for a discount or not
if discount:
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")
