try:
    with open("New Text Document.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error : the file does not exist.")