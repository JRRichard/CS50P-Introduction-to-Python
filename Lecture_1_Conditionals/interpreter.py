# User to enter x as integer, y as operator and z as integer
expression = input("Expression: ")

# Check for first and last numbers inputted and convert to integer
x = float(expression.split()[0])
z = float(expression.split()[-1])

# Look for operator in index "2" to determine action to take
if expression.split()[1]=="+":
    print (x+z)
elif expression.split()[1]=="-":
    print (x-z)
elif expression.split()[1]=="*":
    print (float(x*z))
else:
    print (round(x/z,1))