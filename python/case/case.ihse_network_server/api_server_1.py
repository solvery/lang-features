import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.0.130', 5555)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data_recv in small chunks and retransmit it
        data_send = '220 Service ready\r\n'
        connection.sendall(data_send)
        print >>sys.stderr, 'send "%s"' % data_send
        data_recv = connection.recv(1024)
        print >>sys.stderr, 'recv "%s"' % data_recv

        if data_recv:
            print >>sys.stderr, ''
        else:
            print >>sys.stderr, 'no more data_recv from', client_address
            break
        
    finally:
        # Clean up the connection
        connection.close()

