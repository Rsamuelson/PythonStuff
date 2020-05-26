# IA03 Processing Data in Python

**Due October 21 11:59pm.**

**Submit this assignment via git to your individual private repo (mis407f19-student-xx) in the directory `IA03`.**

**PLEASE DO NOT COMMIT THE IOWA LIQUOR SALES DATA FILE TO YOUR mis407f19-student-xx repo!**

## Introduction

OpenData sources are growing in number. Many governments have "OpenData" initiatives that provide portions of government/public data for public access. It is motivated on the idea that some data should be freely available to everyone. From a government perspective, "opening up" data can also help to initiate innovative uses of public data.

For this assignment you will analyze an OpenData file on liquor purchases made by **Class E** liquor license holders in the State of Iowa.

## Problem 1: 30 pts

Download my copy of the Iowa Liquor Sales dataset for 2018 as a csv file from CyBox for MIS407 at:

[Iowa-Liquor-Sales-2018.csv](https://iastate.box.com/shared/static/d7iwcwn9nizh9yp98pd9879hwq5eamx9.csv)

The file `Iowa-Liquor-Sales-2018.csv` from CyBox contains one year of data out of several years. (If you are curious, the full data can be downloaded from the website
https://data.iowa.gov/Economy/Iowa-Liquor-Sales/m3tr-qhgy -- **but it is 4GB in size, and I don't want you to have to deal with a file so large!**)

**NOTE: PLEASE DO NOT COMMIT THE IOWA LIQUOR SALES DATA FILE TO YOUR mis407f19-student-xx repo!** Downloading 20 copies of the file (and the repo containing a copy of the file) will overload my workstation.

Your task is to write a program that analyzes this file. There are 24 columns in the csv file, of which these are probably the interesting ones:
```
INVOICE_NUM = 0
DATE = 1
STORE_NUM = 2
STORE_NAME = 3
CITY = 5
COUNTY_NUM = 8
COUNTY_NAME = 9
VENDOR_NUM = 12
VENDOR_NAME = 13
ITEM_NUM = 14
ITEM_NAME = 15
BOTTLE_SIZE = 17
SALE = 21
VOLUME_LITERS = 22
VOLUME_GALS = 23
```

Write a program `ia03_1.py` that:
* Asks for the name of the input file
* Opens and reads the file with a CSV reader:
   * Selects only rows for `STORY` county
   * Computes and (at the end) prints these values:
   * **Volume sold by each store in STORY county** in liters *ordered by store name*
   * **Total volume sold by all stores in STORY county** in liters
* Print the computed values on the screen, like this **ficticious** output:
```
Alcohol sales by store in STORY county:
  1. AJ's Liquor III                           11,222.55 liters
  2. Casey's General Store # 2560/ Ames         4,567.89 liters
  3. CVS Pharmacy #10452  /  Ames               3,987.65 liters
  ...
  42. Walgreens #12108 / Ames                   1,222.33 liters
  Total: 654321.123 liters
```
* Commit your program `ia03-01.py` into the `IA03` folder of your student repo for grading.
* Copy, paste, and commit the output of your program into the `IA03` folder file `output-1.txt` to show your program worked.
* Select based on **total volume**, not dollar value. Report only stores in STORY county.

The program must use the `csv` library for file IO. For processing of data, you can use any of the built-in data types (sets, lists, tuples, string, and the various object/structures found in the Collections library). **We are not - at this stage - using numpy, Pandas, or even SQLite to process such data.** We will use these later in the course, but for now I want you to know how to do this assignment using the standard Python library.

*Hints*:
* Don't try to read the entire CSV file using a `list(csvFile)` -- your computer may not have enough memory to load the entire file into a list at once. Instead, use a for loop over your csvFile and process data row-by-row.
* I've counted 44 separate stores that sold liquor in 2018 in Story county
* A per-store dictionary would be an excellent way to hold the data as you sum it. You could make a dictionary by store name, and for each row, if the store is in STORY county, add the liquor volume to the appropriate entry in the dictionary.

## Problem 2: 10 pts

Copy and modify your program to print only the top 5 stores in STORY county by volume.

* Create a copy of your program `ia03_1.py` to `ia03_2.py`
* Update the code in `ia03_2.py` to ask for the name of the input file, open it, read it, process the volume of liters by store in STORY county, and print the *top 5 stores* ordered by volume:
   * *Hint*: The `Counter` class in the python `collections` module can take a dictionary and return a sorted list of the top most common elements in a dictionary. If you accumulated the sales volume by store in a dictionary named ``, you could use code like this:
```
from collections import Counter
...
top_values = Counter(volume_by_store).most_common(5)
```
   * Print the top_values similar to how all stores were printed for task 1 (but don't print the total), like this ficitious sample output:
   ```
   Top 5 stores in STORY county alcohol sales by volume:
        1. Fairway              56,321.00 liters
        2. Kay-Vee              42,456.59 liters
        3. Way-Mart             37,345.80 liters
        4. Stash-N-Go           22,333.53 liters
        5. Cathy's              11,888.34 liters
```
* Commit your program `ia03_2.py` into the `IA03` folder of your student repo for grading.
* Copy, paste, and commit the output of your program in the file `output-2.txt` in the `IA03` folder of your student repo to show your program worked.

## Bonus: 20 pts (optional)

Determine the most popular product (by volume) at each store. Process the input file as before, but for your output, show the most popular product (by volume) for each store.

Sample output (leading digits of volumes left as an indication of the total volume you might expect from a successful run of the program):
```
Most popular product by volume in each store in STORY county:
  1. AJ'S LIQUOR II       Hawkeye Vodka          3,xxx.xx liters
  2. AJ's Liquor / Ames   Hawkeye Vodka            3xx.xx liters
  3. AJ's Liquor III      Paramount Gold Rum     2,xxx.xx liters
  ...
 42. White Oak Station #82 / Nevada Hawkeye Vodka            2xx.xx liters
 43. Yesway Store # 10020/ Story City Hawkeye Vodka          1,xxx.xx liters
 44. goPuff / Ames        Svedka Strawberry Lemonade       8.xx liters
```

Re-use your code from `ia03_1.py` in a new program, but you might use a nested dictionary: products by store for the top-level dictionary, and volume by product for the inner dictionary. Or, you could use a flat dictionary of volumes indexed by store name + product name.

* Name this program `ia03_popular_booze.py`. Capture a copy of your output in the file `ia03_bonus_output.txt` file to show your program worked.
* Commit your program `ia03_popular_booze.py` and your *output* `ia03_bonus_output.txt` file in your `IA03` directory for grading.
