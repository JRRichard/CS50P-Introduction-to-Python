# Ask user question about Great Question of Life and get response
question = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

# Check for answer and return Yes or No
if question.strip() == "42" or question.lower().strip()== "forty-two" or question.lower().strip()== "forty two":
    print ("Yes")
else:
    print ("No")