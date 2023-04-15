import zmq

# initialize ZeroMQ context and create a REQ socket to send messages
context = zmq.Context()
socket = context.socket(zmq.REQ)

# connect to the chat server
print("Connecting to the chat server...")
socket.connect("tcp://node00:5556")

while True:
    # prompt the user to enter a message to send to the chat room
    message = input("Type your message here: ")

    # send the message to the chat room via the server
    socket.send_string(message)

    # wait for a reply from the chat server
    response = socket.recv_string()

    # print the response to the console
    print("Server: %s" % response)