#!/usr/bin/env python

from xylophone.server.server import MockXyloServer

if __name__ == '__main__':
    """
    In this script we show how to start a server that conects with a simulated xylophone. 
    This starts a TCP server that will listen for messages sent with the
    XyloClient.
    """
    server = MockXyloServer(host='localhost', port=8080)
    server.start()

