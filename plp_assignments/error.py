filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as f:
        content = f.read()

    with open("new_" + filename, "w") as f:
        f.write(content.upper())

    print("Modified content written to new_" + filename)

except FileNotFoundError:
    print("Error: File not found.")
except:
    print("An error occurred while reading or writing the file.")
