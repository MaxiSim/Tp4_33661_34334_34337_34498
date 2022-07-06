import json

from socketserver import BaseRequestHandler
from ..xylo.note import XyloNote

class TCPHandler(BaseRequestHandler):

    def handle(self) -> None:
        """A TCP handler responsible for addressing the TCP queries."""
        self.data = self.request.recv(1024).strip()
        if self.data == b'play':
            self.server.xylo.play()
        else:
            note = json.loads(self.data, object_hook=XyloNote.from_json)
            self.server.xylo.send(note)
        self.request.sendall(self.data.upper())

