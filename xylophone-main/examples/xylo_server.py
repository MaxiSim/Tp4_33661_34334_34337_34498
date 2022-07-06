#!/usr/bin/env python

from xylophone.server.server import XyloServer

if __name__ == '__main__':
    """
    In this script we show how to start a server to communicate with the real
    xylophone.
    This starts a TCP server that will listen for messages sent with the XyloClient
    """
    server = XyloServer(host='localhost', port=8080)
    server.start()

