num_students = int(input("enter the number of students:"))
o = 1
while o <= num_students:
    total_grades = 0
    num_subjects =  int(input(f"enter your number of subjects for students {o}: "))

    for p in range(1, num_students +1):
        grade = float(input(f"enter subject {p} grade for students {o}:"))
        total_grades += grade

average_grade = total_grades / num_subjects
print(F"average grade for students {o}: {average_grade:.2f}")
o += 1
