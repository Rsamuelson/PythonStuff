# Control flow and string slicing

For this in-class assignment, follow these instructions:

* In your `mis407f19-student-xx` repository, create a new directory `ICA03`
* Create your program named `parse_string.py` in the `mis407f19-student-xx/ICA03` directory
* Be sure to commit and push your program to Github when you have completed it

## Program Steps

* Ask the user to enter a sentence
* Loop over the characters in the string:
  * If the character is an alphabetic letter, print the string "Letter:" followed by letter and the character's numeric (ordinal) value (examples: 'A' is 65, 'a' is 97)
  * Else if the character is a digit, print "Digit:" followed by the digit
  * Else if the character is whitespace, print "Whitespace"
  * Else, just print "Not letter or digit:" followed by the character

## Sample Runs

A run of the program should look like this:
```
$ python parse_string.py
Enter a sentence: This is a test. #1
Letter: 84
Letter: 104
Letter: 105
Letter: 115
Whitespace
Letter: 105
Letter: 115
Whitespace
Letter: 97
Whitespace
Letter: 116
Letter: 101
Letter: 115
Letter: 116
Not a letter or digit: .
Whitespace
Not a letter or digit: #
Digit: 1
```
