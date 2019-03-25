def get_file_contents(filename):
    try:
        queried_file = open(filename, 'r')

        if queried_file.mode == 'r':
            return queried_file.read()
    except:
        print("There was an issue reading that file")


content = get_file_contents("file-section/text_content.txt")
whoops = get_file_contents("file-section/doesntexist.txt")

print(whoops)
