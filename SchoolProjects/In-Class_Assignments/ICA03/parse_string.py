line = input("Please enter a string: ")
for char in line:
    if char.isalpha():
        print("Letter: {}".format(ord(char)))
    elif char.isdigit():
        print("Digit: {}".format(char))
    elif char.isspace():
        print("Whitespace")
    else:
        print("Not a letter or diget: {}".format(char))