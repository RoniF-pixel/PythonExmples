"""finding the largest, second lagrest and N largest number in a list"""
#the largest
numbers = [55, 27, -97, 12, 2]
minimum = numbers[0]
for i in numbers:
    if i > minimum:
        minimum = i
print("The largest number in the list is:", minimum)
