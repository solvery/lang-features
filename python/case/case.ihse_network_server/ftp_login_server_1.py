import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.0.130', 21)
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

        # Receive the data in small chunks and retransmit it
        ftp_data = '220 Service ready\r\n'
        connection.sendall(ftp_data)
        print >>sys.stderr, 'send "%s"' % ftp_data
        data = connection.recv(1024)
        print >>sys.stderr, 'recv "%s"' % data

        ftp_data = '331 User name ok, need password\r\n'
        connection.sendall(ftp_data)
        print >>sys.stderr, 'send "%s"' % ftp_data
        data = connection.recv(1024)
        print >>sys.stderr, 'recv "%s"' % data

        ftp_data = '230 User logged in\r\n'
        connection.sendall(ftp_data)
        print >>sys.stderr, 'send "%s"' % ftp_data
        data = connection.recv(1024)
        print >>sys.stderr, 'recv "%s"' % data

        ftp_data = '221 Bye\r\n'
        connection.sendall(ftp_data)
        print >>sys.stderr, 'send "%s"' % ftp_data
        data = connection.recv(1024)
        print >>sys.stderr, 'recv "%s"' % data


        if data:
            print >>sys.stderr, ''
        else:
            print >>sys.stderr, 'no more data from', client_address
            break
        
    finally:
        # Clean up the connection
        connection.close()

