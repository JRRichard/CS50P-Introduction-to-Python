# Prompt user input for mass in kilograms
mass = int(input("m: "))

# Use speed of light as 300,000,000 meters per second
c = 300000000

E = mass * c**2

# Return result from user input and calculation for E
print ("E:", E)