import csv
from tkinter import *
from tkinter import messagebox

input_filename = 'test4_input.csv'

def read_file(filename):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        somedata = list(reader)
        print(somedata)

    list1.delete(0,END)
    for i in range(len(somedata)):
        list1.insert(END, somedata[i])
        


def exit_command():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        window.destroy()

window = Tk()

# Display Buttons
b1 = Button(window, text="Exit", width=5, command=exit_command)
b1.grid(row=0, column=2)

############################
# display listbox and attach a scrollbar
list1 = Listbox(window, height=6, width=80)
list1.grid(row=0, column=0, rowspan=6, columnspan=1)

sb1 = Scrollbar(window)
sb1.grid(row=0, column=1, rowspan=6, sticky=N+S+W)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

read_file(input_filename)

window.mainloop()