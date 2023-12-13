"""finding the largest, second lagrest and N largest number in a list"""
#the largest
numbers = [55, 27, -97, 12, 2]
minimum = numbers[0]
for i in numbers:
    if i > minimum:
        minimum = i
print("The largest number in the list is:", minimum)

#second largest
numbers = [55, 27, -97, 12, 2]
# Sort the list in descending order
numbers.sort(reverse=True)
# Check if there are at least two elements in the list
if len(numbers) >= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain a second largest number.")

#N largest
def find_n_largest_elements(lst, n):
 # Sort the list in descending order
 sorted_lst = sorted(lst, reverse=True)
 # Get the first N elements
 largest_elements = sorted_lst[:n]
 return largest_elements
numbers = [70, 10, 35, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98]
# Number of largest elements to find
N = int(input("N =  " ))
# Find the N largest elements from the list
result = find_n_largest_elements(numbers, N)
print(f"The {N} largest elements in the list are:", result)
