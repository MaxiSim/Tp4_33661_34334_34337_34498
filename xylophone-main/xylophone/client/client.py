#!/usr/bin/env python3

import socket
from typing import List

from ..xylo.note import XyloNote
from ..util.logger import logger


class XyloClient:
    def __init__(self, host: str='localhost', port: int=8080):
        """Instantiates an object.

        The object is XyloNote(host, port).

        Args:
            host (str): The host name or IP address of the listening server.
            port (int): The port number in which the server is listening on. 
        """
        self.host = host
        self.port = port


    def play(self) -> None:
        """
        Sends the play command to the XyloServer.
        """
        self._socket_send('play')


    def load(self, notes: List[XyloNote]) -> None:
        """Loads all the written notes into the server.

        Args:
            notes (list[XyloNote]): a list containing all the notes 
        """
        for note in notes:
            self.send(note)


    def send(self, note: XyloNote) -> None:
        """Sends only one note to the server.

        This method sends one note to the server so the server stores it in its
        buffer.

        Args:
            note (XyloNote): a note object.

        Raises:
            ValueError: if it's not a XyloNote, this method fails.
        """
        if not isinstance(note, XyloNote):
            raise ValueError("note is not a XyloNote")

        data = note.to_json()
        self._socket_send(data)


    def _socket_send(self, data: str) -> None:
        """Sends the data to the server using a socket.

        This method sends the bytes representation of the data in utf-8
        using TCP as the L4 protocol.

        Args:
            data (str): the raw data in string format.
        """
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to server and send data
            s.connect((self.host, self.port))
            s.sendall(bytes(data + "\n", "utf-8"))

            # Receive data from the server and shut down
            received = str(s.recv(1024), "utf-8")
            
            logger.debug(received)

