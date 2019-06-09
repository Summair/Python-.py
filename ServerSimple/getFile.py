""" get file  client and service side logic to transfer an arbitrary file from serve to client over a socket; uses a simple control-info protocol

"""



import sys, os, thread, time

from socket import *

def now(): return time.time(time.time())

blocksize = 1024

defaultHost = 'localhost'
defaultPort = '50001'                               #default port and host listerner is set on

helptext = """                                      #you can set a help section on the functions the app can execute
 
server=> getfile.py - mode server             [-port nnn] [-host hhh|localhost]
client=> getfile.py [-mode client] -file fff  [-port nnn] [-host hhh|localhost]
"""

def parsecommandline():
    dict = {}
    args = sys.argv[1:]
    while len(args) >= 2:
        dict[args[0]] = args [1]
        args = args[2:]

    return dict

def client(host, port, filename):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send(filename + '\n')
    dropdir = os.path.split(filename)[1]
    file = open(dropdir, 'wb')
    while True:
        data = sock.recv(blocksize)
        if not data: break
        file.write(data)
    sock.close()
    file.close()
    print 'Client got', filename, 'at', now()


def serverthread(clientsock):
    sockfile = clientsock.makefile('r')
    filename = sockfile.readline()[:1]
    try:
        file = open(filename, 'rb')
        while True:
            bytes = file.read(blocksize)
            if not bytes: break
            sent = clientsock.send(bytes)
            assert sent == len(bytes)
    except:
        print ' Error downloading file on server:', filename
    clientsock.close()


 def server(host, port):
     serversock = socket(AF_INET, SOCK_STREAM) 
     serversock.bind((host, port))
     serversock.listen(5)
     while True:
         clientsock, clientaddr = serversock.accept()
         print 'Server connected by', clientaddr, 'at', now()
         thread.start_new_thread(serverthread, (clientsock,))

def main(args):
    host = args.get('-host', defaultHost)
    port = int(args.get(' -port', defaultPort))

    if args.get('-mode') == 'server':
        if host == 'localhost' : host = ''
        server(host, port)
    elif args.get('-file'):
        client(host, port, args['-file'])

    else:
        print helptext

 if __name__ == '__main__':
    args = parsecommandline()
    main(args)

    
                               








