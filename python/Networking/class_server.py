#!/usr/bin/bash
#############################################
#create socket object bind as server or connect as client
#create ssl_object after socket creation
#verify cert and uathenticity of server
#send a message via ssl_sock_obj
from multiprocessing import Process, Pipe
from _thread import *
import threading
import socket, ssl, argparse
import select, sys

# define socket and and create list
s = socket.socket()
Identifiers = {}


#create a class to handle the socket object
#add error handling within each class that does importance


#   This class lays out the info needed to be passed to the socket
class socket_info:
    def __init__(self, host, port):
        self.host=host
        self.port=port
        
    

#   Runs all the server functions
class server(socket_info):
    #   bind and listen for incomming calls
    def __init__(self,host,port):
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(5)
        

        #   Handle the messages 
    # need to add way to send messages to specific thread defined by a secret or something






       #   Accept conections needs to be passed to the threads function    
class connection_handler:
    print('A connection needs handled')


    def thread_handler(self,conn,addr):
        print("client thread info  {%s}, {%s} " %(addr[0], addr[1]))

#   set this to run for all clients when first connect
        if Identifiers == {}:
            conn.send(b'Welcome to Anon Chat Server you are the first to connect (datetime), Pick an alias :')
            alias = conn.recv(4096)
            Identifiers[alias] = addr[1]
            conn.send(b"We have updated the connections list")
            self.message_handler(conn,addr,alias)

        
            
#   finish private messaging then add broadcast
#   Never forget yourself   !!!        
    def message_handler(self,conn,addr,alias):
        conn.send(b'Broadcast mode or private message mode ?')
        mode = conn.recv(4096)
        conn.send(b'Welcome to Private message mode, Who would you like to talk to ')
        friend = conn.recv(4096)
        


        if friend == 'home':
            conn.send(b'#<$HOME>#')
            option = conn.recv(4096)
            print(option)

            if option == 'private':
                print("oprivate")
                for identity in Identifiers:

                    if Identity == friend:

                        print('friend is in the list now figure out how to send this to specific address')
                        while True:
                            conn.send(b'#<$END>#'  # need to send to specific client on thread
                            data = conn.recv(4096)
                            conn.send(b'%s, you sent :%s ' %(alias,data,friend))
                    else:

                        print('search failed')
           
             
                
          

     

    def accept_conns(self):
        while True:
            self.conn, self.addr = s.accept()
            conn = self.conn 
            addr = self.addr
        
             
            start_new_thread(self.thread_handler,  (conn,addr,)) #open as new thread and execute the client_handler passing client addr info 
#            self.thread_handler(self,conn,addr)

        
        


parser = argparse.ArgumentParser(
            prog="server and client using classes, Pick to run as server or client", epilog="chat application by Jargon314"
            )

parser = argparse.ArgumentParser()
parser.add_argument("stype")
parser.add_argument("address")
parser.add_argument("port", type=int)
args = parser.parse_args()
stype = args.stype
address = args.address
port = args.port
    #print(stype+", "+ address+", "+ str(port))
##################################
#   Need to add processes so each client spawns its own process

if stype == 'server':
    print('Opening a listener')
    do = server(address, port)
    #parent_conn, child_conn = Pipe()
    #p = Process(target=, args=child_conn,)
    #p.start()
    #p.join()
   
if __name__ == '__main__':
    while True:
        dp2 = connection_handler() #    class that handles distribution of individual threads
        dp2.accept_conns()                  # spawns the threads, 
                                    #       add: loginfo, 1 on 1 convo, Identifiers or session keys. 

    


    



###################
# accept connections as a process so you can send messages while accepting
#if __name__ == '__main__':
#    p = Process(target=server)
#    p.start()
#    p.join()

#   NOTES:  add admin login and user login add admin tools for the server updates/notifications
#           Add gui QT or REACT JS
