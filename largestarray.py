"""finding the largest element in an array"""
def find_largest_element(arr):
    if not arr:
        return "Array is empty"
    largest_element = arr[0]
    for element in arr:
        if element > largest_element:
            largest_element = element
    return largest_element

array = [30, 10, 102, 99]
result = find_largest_element(array)
print(f"The largest element in the array is: {result}")
