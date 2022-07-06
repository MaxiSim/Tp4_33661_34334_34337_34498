#!/usr/bin/env python

from typing import Tuple
from socketserver import BaseRequestHandler, TCPServer

from .handler import TCPHandler
from ..xylo.phone import BaseXylo, Xylo, MockXylo


class CustomTCPServer(TCPServer):

    def __init__(self, host_port: Tuple[str, int], handler: BaseRequestHandler, xylo: BaseXylo):
        """Instantiates a custom TPC server.

        Args:
            host_port (Tuple[str, int]): a tuple containing both host and port
            of the server.
            handler: a TCP handler configured to address queries.
            xylo: a Xylo instance to inject to the server.
        """
        super().__init__(host_port, handler)
        self.xylo = xylo


class BaseXyloServer:

    def __init__(self, host: str, port: int):
        """Don't use this method from outside another __init__ method.

        This class should be considered as an abstract class.

        Args:
            host (str): Hostname or IP address to bind the server.
            port (int): Port number to listen to.

        Raises:
            If port is not an integer it will fail.
        """

        if not isinstance(port, int):
            raise TypeError("Port must be an integer")
        
        self.host = host
        self.port = port

    def _start(self, handler: BaseRequestHandler, xylo: BaseXylo):
        """Binds and starts the server.

        Args:
            handler (BaseRequestHandler): a TCP handler to be used.
            xylo (BaseXylo): the xylo instance to be used by the TCP handler.
        """

        with CustomTCPServer((self.host,self.port), handler, xylo) as server:
            server.serve_forever()


class MockXyloServer(BaseXyloServer):

    def __init__(self, host: str='localhost', port: int=8080):
        """Instantiates a mock server.

        Args:
            host (str): Host or IP address to bind to.
            port (int): Port number to listen to.
        """
        super().__init__(host=host, port=port)


    def start(self) -> None:
        """Starts the server."""
        self._start(TCPHandler, MockXylo())


class XyloServer(BaseXyloServer):

    def __init__(self, host: str='localhost', port: int=8080):
        super().__init__(host=host, port=port)


    def start(self):
        """Starts the server"""
        self._start(TCPHandler, Xylo())

