#!/usr/bin/env python

"""
Simple UDP packet forwarder.
Listen to a udp socket, and fires the same packet to remote destination(s)
"""

import socket
import sys, time, string

def sendUDP(remotehost,remoteport,UDPSock,data):
        UDPSock.sendto( data, (remotehost,remoteport))

def serverLoop(listenport,remotes):
        # Set up socket
        UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        UDPSock.bind( ("0.0.0.0",listenport) )
        while 1:
                data, addr = UDPSock.recvfrom(1024)
                if not data: pass
                else:
                        # Send udp packet to remotes...
                        for remote in remotes:
                                sendUDP(remote[0],remote[1],UDPSock,data)
                time.sleep(0.001)

if __name__ == "__main__":
        if len(sys.argv) < 3:
                print "%s listenport remotehost1:port1 remotehostN:portN ..." % sys.argv[0]
                sys.exit(-1)
        listenport = int(sys.argv[1])
        print "Local forward port %d" % listenport
        remotes = []
        for pair in sys.argv[2:]:
                host,port = string.split(pair,":")
                remotes.append( (host,int(port)) )
                print "Adding remote forward %s:%s" % (host,port)
        print "Starting serverloop"
        serverLoop(listenport,remotes)
