age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ")
discount = (age <= 12) or (13 <= age <= 18 and student == "yes")
if discount:
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")
