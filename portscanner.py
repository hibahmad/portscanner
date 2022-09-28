from socket import *

# given IP address input and list of ports
# tcp connection to the port
# look for response TCP ACK response from server

# main method that will try to make the connection: 
# takes a target host and single port as parameters
def connection_scan(tgt_host, tgt_port):
    # test if connection is successful
    try: 
        # A pair (host, port) is used for AF_INET 
        # The socket type should be SOCK_STREAM (the default)
        connection_skt = socket(AF_INET, SOCK_STREAM)

        # define that the connection will connect:
        # takes the target host and target port that will be used to make the connection
        connection_skt.connect((tgt_host, tgt_port))

        # define positive case
        # takes value of target port and inserts it into print
        print('[+]%d/tcp open'% tgt_port)

        # close connection 
        connection_skt.close()
    except: 
        print('[-]%d/tcp closed'% tgt_port)

# define port scanner method - used to avoid DNS lookup 
# new parameter for target ports - want to input list of ports to scan rather than continusously calling it
def port_scanner(tgt_host, tgt_ports):
    # try to translate host name by getting IP
    try: 
        tgt_IP = gethostbyname(tgt_host)
    except: 
        print('[-] cannot resolve %s '% tgt_host)
        # return to get back
        return
    # given that we have IP:
    try: 
        # get host name by IP address
        tgt_name = gethostbyaddr(tgt_IP)
        # new line while it is looping
        print('\n[+] scan result of: %s ' % tgt_name[0])
    except: 
        print('\n[+] scan result of: %s ' % tgt_IP)
    # so we only do this once a second
    setdefaulttimeout(1)
    # loop over list of ports provided in tgt_ports
    # this method calls connection_scan method and 
    # prints whether the port is open or closed 
    # along with a line stating what port is currently being scanned
    for tgt_port in tgt_ports: 
        print('scanning port: %d'% tgt_port)
        connection_scan(tgt_host, int(tgt_port)) 

# used to execute code directly rather than from command line
# call method
if __name__ == '__main__': 
    # google IP address as target host, and target port is port 80
    connection_scan('216.58.207.238', 80)
    port_scanner('google.com', (80, 22))