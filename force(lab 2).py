print("NEWTONS SECOND LAW OF MOTION")
print("-------------------------------")
print("The missing value")
print("1. mass (m)")
print("2. acceleration (a)")
print("3. force (f)")
missing_value_choice = input("Enter the option number for the missing valuee")
if missing_value_choice == "1":
    a = float(input("Enter acceleration (a): ")) 
    f = float(input("Enter force (f): "))
    m = f/a
    print(f"mass (M) = {m}")

elif missing_value_choice == "2":
    m = float(input("Enter mass (m): "))
    f = float(input("Enter force (f) "))
    a = f/m
elif missing_value_choice == "3":    
    m = float(input("Enter mass (m) "))
    a = float(input("Enter acceleration (a) :"))
    f = float(input("Enter force (f) "))
    print(f"force (f)= {f}")
else:
    print("invalid")
