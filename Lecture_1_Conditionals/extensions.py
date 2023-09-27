# Get user input for file name with extension
file_name = input("File name: ")

# Check for end/suffix of the file with endswith
if file_name.strip().lower().endswith(".gif"):
    print("image/gif")
elif file_name.strip().lower().endswith(".jpg") or file_name.strip().lower().endswith(".jpeg"):
    print("image/jpeg")
elif file_name.strip().lower().endswith(".png"):
    print("image/png")
elif file_name.strip().lower().endswith(".pdf"):
    print("application/pdf")
elif file_name.strip().lower().endswith(".txt"):
    print("text/plain")
elif file_name.strip().lower().endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")