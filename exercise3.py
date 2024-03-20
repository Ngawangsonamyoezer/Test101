for i in range(1, 10):
    if i == 7:
        break  # Break out of the outer loop when reaching 7
    print("Outer Loop:", i)
    j = 1
    while j <= 9:
        if j != 3:
            print("Inner Loop:", j)
        j += 1
