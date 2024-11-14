import socket

def port_scan():
    link = input("Enter the link here: ")
    host = socket.gethostbyname(link)
    res = 'a'
    while(res != "bye"):
        min = input("Enter the lowest limit of range: ")
        max = input("Enter the highest limit of range: ")
        for port in range(int(min), int(max)):
            try:
                client_socket = socket.socket()
                print("Trying to connect ", host, " on port", port, "......")
                if client_socket.connect_ex((host, port)) == 0:
                    print("Connection to ", host,"on port", port, "was SUCCESSFUL")
                else:
                    print("Connection to ", host,"on port", port, "was FAILED")
                    port = port + 1
                    client_socket.close()
            except socket.error:
                print("Connection to ", host,"on port", port, "was an ERROR")
            port = port + 1
            client_socket.close()
        res = input("The Port Scanning has concluded. To exit, please type bye. However if you would like to continue with different input, press y")
    print("Scanner has exited")
    
if __name__ == '__main__':
    port_scan()