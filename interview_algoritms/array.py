import numpy as np

#ASC
sort_arry = [1, 2, 4, 6, 1, 2, 9]
sort_arry.sort()
print("Sorted array using sort():", sort_arry)

#DESC
sort_arry_reverse = [1, 2, 4, 6, 1, 2, 9]
sort_arry_reverse.sort(reverse=True)
print("Sorted reverse array using sort():", sort_arry_reverse)


# Example numpy array
arr = np.array([5, 2, 9, 1, 5, 6])
# Using numpy's sort function
sorted_arr = np.sort(arr)
print("Original numpy array:", arr)
print("Sorted numpy array using np.sort():", sorted_arr)


# Maximum element in array
def find_max(arr):
    return max(arr)
arr = [5, 3, 8, 4, 2]
print(find_max(arr))  # Output: 8