#convert kilometers to miles
kilometers = float(input("Enter distance in kilometers: "))
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")
#miles to kilometers
miles = float(input("Enter distance in miles: "))
conversion_factor = 0.621371
kilometers = miles / conversion_factor
print(f"{miles} miles is equal to {kilometers} kilometers")