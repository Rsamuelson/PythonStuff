import csv
from tkinter import *
from tkinter import messagebox
import os

input_filename = 'CornProduction2008-2018.csv'
columnDictionary = {"YEAR" : 0, "COUNTY": 1, "VALUE": 2}
totalCornAmount = 0

def read_cornprod(filename, county):
    """
    Read the county production from the specified file.
    Return the total production for the specified county.
    """
    ProdAmount = 0
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[columnDictionary.get('COUNTY')] == county:
                countyValue = int(row[columnDictionary.get("VALUE")])
                ProdAmount = ProdAmount + countyValue
    return ProdAmount

def report_command():
    """ Search for the specified county data in county_text field
        and show the total production for the county in total_prod_text. """

    county = county_text.get()
    totalCornAmount = 0
    totalCornAmount = read_cornprod(input_filename, county.upper())
    e2.delete(0,END)
    e2.insert(0, totalCornAmount)
    

def clear_command():
    e1.delete(0,END)
    e2.delete(0,END)


def exit_command():
    window.destroy()


window = Tk()  # TK method that creates a windows object
window.wm_title("County Corn Production Report")
#########
# Display Titles
l1 = Label(window, text="County")
l1.grid(row=0, column=0)

l2 = Label(window, text="Total Production")
l2.grid(row=1, column=0)

#########
# Display Titles# Display text entry fields
county_text = StringVar()
e1 = Entry(window, textvariable=county_text, width=35)
e1.grid(row=0, column=1)

total_prod_text = StringVar()
e2 = Entry(window, textvariable=total_prod_text, width=15)
e2.grid(row=1, column=1)

# Display Buttons
b1 = Button(window, text="Report", width=10, command=report_command)
b1.grid(row=2, column=0)
b1 = Button(window, text="Clear", width=10, command=clear_command)
b1.grid(row=2, column=1)
b6 = Button(window, text="Exit", width=10, command=exit_command)
b6.grid(row=2, column=2)

window.mainloop()