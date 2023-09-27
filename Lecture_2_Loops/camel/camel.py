# User input in camelCase and have cursor at the end of snake_case for subsequent printing
camel_input = input("camelCase: ")
print("snake_case: ", end="")

# If lowercase, continue adding else if uppercase, add "_", lower character and continue adding
for l in camel_input:
    if l.islower():
        print(l, end="")
    else:
        print("_" + l.lower(), end="")
print()


