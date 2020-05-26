# Command-Line Arguments

The `sys` module provides useful system-specific functionality, including obtaining the strings from the command line:
```python
import sys

print(sys.argv)
```

We've seen an example in the lecture notes about using `argv` from the `sys` module to access string inputs given on the command line. This exercise will involve taking input from the command line and using it.

## ICA04 task

**In your checkout of the `mis407f19-student-xx` repo, be sure to `git pull` before starting this assignment.**

Create the `ICA04` directory in your `mis407f19-student-xx` repo and, in it, write a program `cmd_calc.py` that:
* If there are three strings on the command line:
  * Check the second string for `+`, `-`, `*`, or `/`, and depending on the symbol, print the result of the arithmetic operation on the first and third strings.
* Otherwise, print an error message `Need to provide three arguments: number [+-*/] number`

For example, running the program will produce results like this (note that the `*` has to be quoted on the command line):
```
$ python cmd_calc.py
Need to provide three arguments: number [+-*/] number
$ python cmd_calc.py 1 + 2
1.0 + 2.0 = 3.0
$ python cmd_calc.py 1 / 2
1.0 / 2.0 = 0.5
$ python cmd_calc.py 1 "*" 2
1.0 * 2.0 = 2.0
```

**Write your program in the file `cmd_calc.py` in your mis407f19-student-xx repository in the subdirectory `ICA04`, and be sure to commit and push it when you have completed it.**
