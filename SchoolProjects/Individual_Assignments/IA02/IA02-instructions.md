
# IA02: Reading and Writing Files

**Due October 7 11:59pm.**

**Submit this assignment via git to your individual private repo (mis407f19-student-xx) in the directory `IA02`.**

Write four small programs that use the given `sample.csv` file for input. You can look back at examples from c12-csv_files/sample_code/csv4b.py for an example that read a CSV file, and csv6.py that read one CSV file and wrote another.

1. `ia02_1.py`:
Write a program that reads each row of `sample.csv` and prints the row's data on the screen.

2. `ia02_2.py`:
Write a program that reads each row of `sample.csv` and writes *every second row* in CSV format to a file called `second_row.csv`. In other words, don't write the first row, third row, fifth row, and so on.

3. `ia02_3.py`:
Write a program that reads each row of `sample.csv` and the writes only the contents of the first, second, and last columns to a file called `selected_cols.csv`.

4. `ia02_4.py`:
Write a program that reads each row of `sample.csv` and counts the number of times `MN` and `MO` were found in the `state` column. Print the totals on the screen, like this (your value for N should appear in the output):
```
MN: total = N
MO: total = N
```

Included in your submission should be the four `py` files (`ia02_1.py`, `ia02_2.py`, `ia02_3.py`, `ia02_4.py`) and the two output files (`second_row.csv` and `selected_cols.csv`)
