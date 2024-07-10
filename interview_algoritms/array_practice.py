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


# Dublicates
from collections import Counter

def find_duplicates(arr):
    element_count = Counter(arr)
    duplicates = [item for item, count in element_count.items() if count > 1]
    return duplicates

# Example usage
arr = [1, 2, 3, 4, 5, 6, 2, 3, 4]
print("Duplicates:", find_duplicates(arr))
# Output: [2, 3, 4]



#bubble sorting

def bubble_arr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n -i -1):
            if arr[j] > arr[j +1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

sort = [12, 34, 54, 32, 56, 76, 34]
bubble_arr(sort)
print("This is bubble sorting", sort)



# Find Duplicates in a List
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

print(find_duplicates([1, 2, 3, 4, 4, 5, 6, 6]))  # Output: [4, 6]
























def find_dublicates3(dub3):
    first = set()
    second = set()
    for item in dub3:
        if item in first:
            second.add(item)
        else:
            first.add(item)
    return list(second)

z = ['A', 'B', 'C', 'D', 'A', 'a', 'a', 2, 3, 4, 2]
result = find_dublicates3(z)
print('dublicares:', result)

def bubbe_search(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n -i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

z = [2, 3, 2, 4, 545, 45, 45, 32, 343, 34, 554, 56]
bubbe_search(z)
print('My bubble search', z)
























