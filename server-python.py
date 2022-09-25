###############################################################################
# server-python.py
# Name:
# NetId:
###############################################################################

import sys
import socket

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10
#FORMAT = 'utf-8'


def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    try: 
        host = "127.0.0.1"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creating a new stream socket where INET stands for the ipv4 

        s.bind((host, server_port)) #binding the socket to the host ip and the server port, in our case the host ip is 127.0.0.1
   
        s.listen(QUEUE_LENGTH) #queued connections in the server where the maximum number of connections allowed are 10 as specified by QUEUE_LENGTH = 10 
   
        connected = True #new socket is connected
    except:
        print("Socket not created")
    while connected: 
        c,addr = s.accept() #accepting a new client connection
        try:
            message_length = c.recv(RECV_BUFFER_SIZE) #receiving the message from the client with max buffersize specified by RECV_BUFFER_SIZE = 2048
            while message_length:#iterating through the message and sending message of BufferSize till the message is complete
                if message_length !="": 
                    sys.stdout.buffer.write(message_length)
                    sys.stdout.flush()
                    message_length = c.recv(RECV_BUFFER_SIZE) 
        except:
            print("Error : Message not received")

                
        
       
        c.close() #closing the connection after the messages are sent.               

pass


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)
       



if __name__ == "__main__":
    main()
