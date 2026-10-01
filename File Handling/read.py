file = open('New Text Document.txt', "r")
content = file.read()
print(content)
# for line in file:
#    # it prints each line removing unnecessary spaces or new line using this strip function
#     print(line.strip())
file.close()