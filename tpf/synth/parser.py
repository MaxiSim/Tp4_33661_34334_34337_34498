import argparse
import numpy as np
from instrument import Instrument

def main() -> None:
    # Initialize argparse object
    parser = argparse.ArgumentParser(description='Recieves the input and output files, in order to run the program.')
    
    # Add arguments
    parser.add_argument('-sn', '--song_name', type = str, help = 'name of the song')
    parser.add_argument('-in', '--instrument_name', type = str, help = 'name of the instrument')
    parser.add_argument('-p', '--music_sheet', help = 'path to the music sheet file')
    parser.add_argument('-i', '--instrument', help = 'path to the file with the instrument')
    parser.add_argument('-o', '--output', help = 'path to the output wavefile')
    parser.add_argument('-f', '--frequency', default = 48000, type = int , help = 'frequency of output')
    
    # Parsing of the arguments
    args = parser.parse_args()
    instrument_name = args.instrument_name
    instrument_name = Instrument(args.instrument_name, args.instrument, args.output)
    instrument_name.read_file()
    
    # print(instrument_name.harmonics)
    
    # print(instrument_name.mods)
    
    instrument_name.synthetise('A3', 2.0)
    # instrument_name.set_functions()

if __name__ == '__main__':
    main()