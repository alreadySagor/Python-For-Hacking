# File reader with error handling.

def file_reader(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File Content.")
            print(content)
    except FileNotFoundError:
        print(f"Error!!!\nThe file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpect error occured.")
file_reader("New Text Document.txt")