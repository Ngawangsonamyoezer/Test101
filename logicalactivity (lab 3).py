
age = int(input("Enter your age: "))
<<<<<<< HEAD


student = input("Are you a student? (yes/no): ")

discount = (age <= 12) or (13 <= age <= 18 and student == "yes")

=======
student = input("Are you a student? (yes/no): ")
discount = (age <= 12) or (13 <= age <= 18 and student == "yes")
>>>>>>> 85b0b010da22e57ac2bb0800bc432d8da9d6c453
if discount:
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")

