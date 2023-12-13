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
