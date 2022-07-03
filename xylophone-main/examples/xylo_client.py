#/usr/bin/env python

from xylophone.client import XyloClient
from xylophone.xylo import XyloNote


if __name__ == '__main__':
    notes = [
            XyloNote('A4', 1.5, 90),
            XyloNote('A4', 2.3, 90),
            XyloNote('G#6', 5.33333, 90),
            XyloNote('A4', 10.01, 90),
            ]

    client = XyloClient(host='localhost', port=8080)
    client.load(notes)
    client.play()

