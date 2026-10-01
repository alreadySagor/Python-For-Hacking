# using 'with' to open a file

# with statement ensures the file is closed automatically after use
with open('New Text Document.txt', "r") as file:
    content = file.read()
    print(content)