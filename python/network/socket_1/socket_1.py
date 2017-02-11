import socket  
  
def print_machine_info():  
    host_name = socket.gethostname()  
    ip_address = socket.gethostbyname(host_name)  
    print ("host name is %s " %host_name)  
    print ("ip address is %s" %ip_address)  
  
def convert_integer():  
    data = 1234  
    # 32 bit  
    print("original: %s => Long host byte order: %s, Network byte order: %s"  
        % (data, socket.ntohl(data), socket.htonl(data)))  
    # 16 bit  
    print("original: %s => Short host byte order: %s, Network byte order: %s"  
        % (data, socket.ntohs(data), socket.htons(data)))  
    data1 = socket.htonl(data)  
    data2 = socket.ntohl(data1)  
    print("%s %s %s" %(data,data1,data2))  

if __name__ == '__main__':  
    print_machine_info()
    convert_integer()
