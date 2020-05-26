from tkinter import *
from tkinter import messagebox

def ComputePayment():
    List.delete(0, END)
    rate = rateText.get()
    years = yearText.get()
    amount = amountText.get()

    monthlyrate = float(rate) / 12.0
    months = int(years) * 12
    payment = float(amount) * ((monthlyrate * (1 + monthlyrate) ** months) / ((1 + monthlyrate) ** months - 1))

    balance = float(amount)
    total_interest = 0
    List.insert(END, "Month Payment Principal Interest Balance")
    for month in range(months):
        interest = balance * monthlyrate
        principal = payment - interest
        balance = balance - principal
        total_interest += interest
        List.insert(END, "{month} {payment} {principal} {interest} {balance}".format(month=month + 1, payment=payment, principal=principal, interest=interest, balance=balance))

    e4.configure(state='normal')
    e4.delete(0, END)    
    e4.insert(0, total_interest)
    e4.configure(state='readonly')

    e5.configure(state='normal')
    e5.delete(0, END)
    e5.insert(0, payment)
    e5.configure(state='readonly')
#     print("{} {}".format(total_interest, payment))
    
def Clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    List.delete(0, END)

    e4.configure(state='normal')
    e4.delete(0, END)    
    e4.configure(state='readonly')

    e5.configure(state='normal')
    e5.delete(0, END)
    e5.configure(state='readonly')
    

def Exit():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        window.destroy()




window = Tk()

#labels
yearLabel = Label(window, text="Years")
yearLabel.grid(row=0,column=0)

AmountLabel = Label(window, text="Amount")
AmountLabel.grid(row=1,column=0)

rateLabel = Label(window, text="Rate")
rateLabel.grid(row=2,column=0)

paymentLabel = Label(window, text="Payment")
paymentLabel.grid(row=0,column=2)

totalInterestLabel = Label(window, text="total_interest")
totalInterestLabel.grid(row=1,column=2)

#Text Box
yearText = StringVar()
e1=Entry(window,textvariable=yearText)
e1.grid(row=0,column=1)

amountText = StringVar()
e2=Entry(window,textvariable=amountText)
e2.grid(row=1,column=1)

rateText = StringVar()
e3=Entry(window,textvariable=rateText)
e3.grid(row=2,column=1)

paymentOutputText = StringVar()
e4=Entry(window,textvariable=paymentOutputText, state='readonly')
e4.grid(row=0,column=3)

totalInterestOutputText = StringVar()
e5=Entry(window,textvariable=totalInterestOutputText, state='readonly')
e5.grid(row=1,column=3)

#list
List = Listbox(window, height=10, width=90)
List.grid(row=3, column=0, rowspan=4, columnspan=4 )

sb1 = Scrollbar(window)
sb1.grid(row=3, column=3, rowspan=4, sticky=N+S+E)

List.configure(yscrollcommand=sb1.set)
sb1.configure(command=List.yview)

#buttons
b1=Button(window, text="Compute", width=12, command=ComputePayment)
b1.grid(row=3, column=4)
b2=Button(window, text="Clear", width=12, command=Clear)
b2.grid(row=4, column=4)
b3=Button(window, text="Exit", width=12, command=Exit)
b3.grid(row=5, column=4)


window.mainloop()