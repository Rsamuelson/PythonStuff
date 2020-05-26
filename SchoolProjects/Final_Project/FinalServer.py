from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)

        client.send(bytes("Welcome to ZlackChat! Type your name and press enter!", "utf8"))
        addresses[client] = client_address

        Thread(target=handle_client, args=(client,)).start()

def accept_incoming_connections_it():
    while True:
        it_client, it_client_address = IT.accept()
        print("%s:%s has connected." % it_client_address)

        it_client.send(bytes("Welcome to IT, What should we call you?", "utf8"))

        Thread(target=handle_client_it, args=(it_client,)).start()
        

def accept_incoming_connections_mgmt():
    while True:
        mgmt_client, mgmt_client_address = MGMT.accept()
        print("%s:%s has connected." % mgmt_client_address)

        mgmt_client.send(bytes("Welcome to Management, What should we call you?", "utf8"))

        Thread(target=handle_client_mgmt, args=(mgmt_client,)).start()
        


def accept_incoming_connections_rnd():
    while True:
        rnd_client, rnd_client_address = RND.accept()
        print("%s:%s has connected." % rnd_client_address)

        rnd_client.send(bytes("Welcome to Management, What should we call you?", "utf8"))

        Thread(target=handle_client_rnd, args=(rnd_client,)).start()
        


def handle_client(client):  # Takes client socket as argument.

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            #client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            #print("%s:%s has disconnected." % addresses[clients.keys().index(name)])
            break

def handle_client_it(it_client):
    name = it_client.recv(BUFSIZ).decode("utf8")
    it_clients[it_client] = name
    
    while True:
        msg = it_client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            it_broadcast(msg, name+": ")
        else:
            #it_client.send(bytes("{quit}", "utf8"))
            it_client.close()
            del it_clients[it_client]
            it_broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

def handle_client_mgmt(mgmt_client):
    name = mgmt_client.recv(BUFSIZ).decode("utf8")
    mgmt_clients[mgmt_client] = name

    while True:
        msg = mgmt_client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            mgmt_broadcast(msg, name+": ", )
        else:
            #mgmt_client.send(bytes("{quit}", "utf8"))
            mgmt_client.close()
            del mgmt_clients[mgmt_client]
            mgmt_broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

def handle_client_rnd(rnd_client):
    name = rnd_client.recv(BUFSIZ).decode("utf8")
    rnd_clients[rnd_client] = name

    while True:
        msg = rnd_client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            rnd_broadcast(msg, name+": ", )
        else:
            #rnd_client.send(bytes("{quit}", "utf8"))
            rnd_client.close()
            del rnd_clients[rnd_client]
            rnd_broadcast(bytes("%s has left the chat." % name, "utf8"))
            break
  


def broadcast(msg, prefix=""):  # prefix is for name identification.
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

def mgmt_broadcast(msg, prefix=""):  # prefix is for name identification.
    for sock in mgmt_clients:
        sock.send(bytes(prefix, "utf8")+msg)

def it_broadcast(msg, prefix=""):  # prefix is for name identification.
    for sock in it_clients:
        sock.send(bytes(prefix, "utf8")+msg)

def rnd_broadcast(msg, prefix=""):  # prefix is for name identification.
    for sock in rnd_clients:
        sock.send(bytes(prefix, "utf8")+msg)


        
clients = {}
mgmt_clients = {}
it_clients = {}
rnd_clients = {}

addresses = {}
mgmt_addresses = {}
it_addresses = {}
rnd_addresses = {}

HOST = ''
PORT = 21000
MGMT_PORT = PORT + 1
IT_PORT = MGMT_PORT + 1
RND_PORT = IT_PORT + 1
BUFSIZ = 1024

ADDR = (HOST, PORT)
MGMT_ADDR = (HOST, MGMT_PORT)
IT_ADDR = (HOST, IT_PORT)
RND_ADDR = (HOST, RND_PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
MGMT = socket(AF_INET, SOCK_STREAM)
IT = socket(AF_INET, SOCK_STREAM)
RND = socket(AF_INET, SOCK_STREAM)

SERVER.bind(ADDR)
MGMT.bind(MGMT_ADDR)
IT.bind(IT_ADDR)
RND.bind(RND_ADDR)

if __name__ == "__main__":

    SERVER.listen(10)
    MGMT.listen(10)
    IT.listen(10)
    RND.listen(10)

    print("Waiting...")

    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    MGMT_ACCEPT_THREAD = Thread(target=accept_incoming_connections_mgmt)
    IT_ACCEPT_THREAD = Thread(target=accept_incoming_connections_it)
    RND_ACCEPT_THREAD = Thread(target=accept_incoming_connections_rnd)


    ACCEPT_THREAD.start()
    MGMT_ACCEPT_THREAD.start()
    IT_ACCEPT_THREAD.start()
    RND_ACCEPT_THREAD.start()

    print("Server is Running!")

    # MGMT_ACCEPT_THREAD.join()
    # IT_ACCEPT_THREAD.join()
    # RND_ACCEPT_THREAD.join()
    ACCEPT_THREAD.join()



    SERVER.close()
    MGMT.close()
    IT.close()
    RND.close()
