try:
    # Writing multiple lines
    print("Enter text to write to the file (type 'END' to stop):",end="")

    with open("output.txt", "w") as file:
        while True:
            line = input()
            if line.upper() == "END":
                break
            file.write(line + "\n")

    print("Data successfully written to output.txt.")

    # Appending multiple lines
    print("\nEnter additional text to append (type 'END' to stop):",end="")

    with open("output.txt", "a") as file:
        while True:
            line = input()
            if line.upper() == "END":
                break
            file.write(line + "\n")

    print("Data successfully appended.")

    # Reading final content
    print("\nFinal content of output.txt:")

    with open("output.txt", "r") as file:
        print(file.read())

except Exception as e:
    print(f"An error occurred: {e}")