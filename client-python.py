###############################################################################
# client-python.py
# Name:
# NetId:
###############################################################################

import sys
import socket

SEND_BUFFER_SIZE = 2048

def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a new socket
        s.connect((server_ip, server_port)) #connecting the socket to 127.0.0.1 and the port number taken as the input
    except:
        print("Socket not created")
    
    try:
        message_length = sys.stdin.buffer.read(SEND_BUFFER_SIZE) #reading the message from the input test file
        while message_length: #Iterate through the message_length
            s.sendall(message_length) #send the message to the server socket
            message_length = sys.stdin.buffer.read(SEND_BUFFER_SIZE) 
    except:
        print("Message not sent")
   
    s.close()#closing the socket
 
pass


def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()
