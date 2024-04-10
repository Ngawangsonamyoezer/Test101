def bubble_sort(num):
    for i in range(0,7,-1):
        for j in range(i):
            if num[j] > num[j + 1]:
                # Swap elements
                num[j], num[j + 1] = num[j + 1], num[j]

num = [5, 3, 8, 6, 7, 2]
bubble_sort(num)
print("Sorted array:", num)
