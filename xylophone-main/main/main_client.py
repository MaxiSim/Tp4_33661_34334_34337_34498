from xylophone.client import XyloClient
from xylophone.xylo import XyloNote
import argparse
import note_reader

def main():
    """
    The main function.
    Runs the program.
    """
    # Initialize argparse object
    parser = argparse.ArgumentParser(description='Recieves the input and output files, in order to run the program.')
    
    # Add arguments
    parser.add_argument('-p', '--music_sheet', help = 'path to the music sheet file')
    
    args = parser.parse_args()
    xylophone = note_reader.Xylophone(args.music_sheet)
    notes = xylophone.get_notes()
    
    # print(notes)

    client = XyloClient(host='localhost', port=8080)
    client.load(notes)
    client.play()
    
    
    
if __name__ == '__main__':
    main()