def main():
    # Output using our "convert" function
    prompt = input()
    convert(prompt)

# Define the "convert" function
def convert(notes):
    print(notes.replace(":)", "🙂").replace(":(", "🙁"))

main()