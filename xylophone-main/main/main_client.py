from xylophone.client import XyloClient
from xylophone.xylo import XyloNote


if __name__ == '__main__':
    notes = []
            

    client = XyloClient(host='localhost', port=8080)
    client.load(notes)
    client.play()