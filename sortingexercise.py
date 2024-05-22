def quicksort(arr):
    """Quick sort algorithm to sort the array in ascending order."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def replace_elements(arr, target, replacement):
    """Replace all occurrences of target with replacement in the array."""
    return [replacement if x == target else x for x in arr]

def main():
    user_input = input("Enter an array of integers separated by spaces: ")
    arr = list(map(int, user_input.split()))

    sorted_arr = quicksort(arr)
    print(f"Sorted array: {sorted_arr}")

    target = int(input("Enter the target element to replace: "))

    if target in sorted_arr:
        replacement = int(input("Enter the replacement element: "))
  
        modified_arr = replace_elements(sorted_arr, target, replacement)
        print(f"Modified array: {modified_arr}")
    else:
        print(f"Target element {target} not found in the array.")

main()  