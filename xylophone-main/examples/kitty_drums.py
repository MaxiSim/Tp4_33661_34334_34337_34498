#/usr/bin/env python

from xylophone.client import XyloClient
from xylophone.xylo import XyloNote


if __name__ == '__main__':
    """This example is used to try out the a set of two servos.
    In this case, the hardware used is the "kitty on drums".
    For more information, look at this link: TODO

    The notes that can only be sent to the kitty are: C7 and B6.
    """
    notes = [
            XyloNote('B6', 1.5, 90),
            XyloNote('C7', 2.3, 90),
            XyloNote('B6', 5.33333, 90),
            XyloNote('C7', 10.01, 90),
            ]

    client = XyloClient(host='localhost', port=8080)
    client.load(notes)
    client.play()

