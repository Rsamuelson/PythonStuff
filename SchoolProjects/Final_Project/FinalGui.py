from tkinter import *
from tkinter import messagebox
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread




HOST = input('Enter host: ')
PORT = input('Enter port: ')

# HOST = '10.29.166.66'

if not PORT:
    PORT = 21000
else:
    PORT = int(PORT)

MGMT_PORT = int(PORT) + 1
IT_PORT = MGMT_PORT + 1
RND_PORT = IT_PORT + 1

roomNameList = ['Home','Management','IT','Research & Development']
roomPortList = [PORT,MGMT_PORT,IT_PORT,RND_PORT] # 1 - 4 are just temp values, Need to change to acutally port numbers
selectedPort = roomPortList[0] # default to the first room
CurrentRoom = "Home"





def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            list2.insert(END, msg)
        except OSError:  # Possibly client has left the chat.
            break

def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = message_text.get()
    message_text.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        window.quit()

def on_closing(event=None):
    """This function is to be called when the window is closed."""
    message_text.set("{quit}")
    send()

def clear_command():
    message_text.set("")


# This Method set the 
def set_port_num(event):
    index = list1.curselection()[0]
    RoomName = list1.get(index)
    print(RoomName)
    # if(RoomName != CurrentRoom):
    CurrentRoom = RoomName
    changeConnectionPort(CurrentRoom)


# need to code to change 
def changeConnectionPort(CurrentRoom):
    global HOST
    global PORT
    global MGMT_PORT
    global IT_PORT
    global RND_PORT
    global ADDR
    global client_socket
    client_socket.close()
    if CurrentRoom == "Home":
        list2.delete(0,END)
        print("Connecting to Home")
        client_socket = socket(AF_INET, SOCK_STREAM)
        
        # client_socket.close()
        ADDR = ("127.0.0.1", 21000)
        client_socket.connect(ADDR)
    
    if CurrentRoom == "Management":
        list2.delete(0,END)
        print("Connecting to Management")
        client_socket = socket(AF_INET, SOCK_STREAM)
        # client_socket.close()
        ADDR = ("127.0.0.1", 21001)
        try:
            client_socket.connect(ADDR)
        except Exception as e:
            print(e)

    if CurrentRoom == "IT":
        list2.delete(0,END)
        print("Connecting to IT")
        client_socket = socket(AF_INET, SOCK_STREAM)
        # client_socket.close()
        ADDR = ("127.0.0.1", 21002)
        client_socket.connect(ADDR)

    if CurrentRoom == "Research & Development":
        list2.delete(0,END)
        print("Connecting to Research & Development")
        client_socket = socket(AF_INET, SOCK_STREAM)
        # client_socket.close()
        ADDR = ("127.0.0.1", 21003)
        client_socket.connect(ADDR)



def FillList1():
    for name in roomNameList:
        list1.insert(END, name)

window=Tk() # TK method that creates a windows objective
window.wm_title("Zlack Chat")

l1=Label(window, text="Chat Rooms")                  # chat room label
l1.grid(row=0,column=0, columnspan = 2, pady = 10)

l2=Label(window, text="Chat")                                  # chat list label
l2.grid(row=0,column=3, columnspan = 2)

l4=Label(window, text="Message")                               # message label
l4.grid(row=3,column=3, sticky = W, padx= 10, pady = (10,0))

# Display Titles# Display text entry fields          textvariable=Chat_rooms_text,
Chat_rooms_text=StringVar()
list1=Listbox(window, width=45, height = 20)                               # chat room list box
list1.grid(row=1,column=0, columnspan = 2, padx = (10,0))

# FillList1()

list1.bind("<<ListboxSelect>>", set_port_num)

message_text=StringVar()
message_text.set("Enter your message here.")
e4=Entry(window,textvariable=message_text, width = 70)          # message entry 
e4.grid(row=3, column=3, columnspan = 2, sticky = E, pady = (10,0))
e4.bind("<Return>", send)


# display listbox and attached a Scrollbar
list2=Listbox(window, width = 80, height = 20)                               # message feed/history
list2.grid(row=1, column=3, columnspan = 2, padx = (10,0)) # we want to span across multiple rows and columns



sb1 = Scrollbar(window)                                         # chat list scroll bar
sb1.grid(row=1, column=2, rowspan=2, sticky=N+S+W)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

sb2 = Scrollbar(window)
sb2.grid(row=1, column=5, rowspan=2, stick=N+S+W, padx=(0,10))

list2.configure(yscrollcommand=sb2.set)
sb2.configure(command=list2.yview)

# Display Buttons
b2=Button(window, text="Clear", width=15, command=clear_command)        # clear button
b2.grid(row=4, column=3, pady = 10, padx = (250, 0))
b3=Button(window, text="Enter", width= 15, command=send)       # enter button
b3.grid(row=4, column=4, sticky = E, pady = 10)



for name in roomNameList:
    list1.insert(END, name)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

window.mainloop()
