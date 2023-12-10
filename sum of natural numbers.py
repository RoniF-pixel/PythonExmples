"""calculating sum of natural numbers"""
limit = int(input("Enter the limit: "))
thesum = 0
for i in range(1, limit + 1):
    thesum += i
print("The sum of natural numbers up to", limit, "is:", thesum)