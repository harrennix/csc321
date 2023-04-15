import zmq

# initialize ZeroMQ context and create a REP socket to receive messages
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

# wait for messages from the chat client
while True:
    message = socket.recv_string()

    # prompt the user to enter a message to send back to the chat client
    reply = input("Type your message here: ")

    # send the reply message back to the client
    socket.send_string(reply)