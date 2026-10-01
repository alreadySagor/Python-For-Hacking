def countwordsinfile(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            print(f"the file '{filename}' contains {len(words)} words.")
    except FileNotFoundError:
        print(f"the file '{filename} does not exist.")
countwordsinfile("words.txt")