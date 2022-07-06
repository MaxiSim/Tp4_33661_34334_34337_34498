import argparse
from synthetizer import Track
import waver

def main():
    """
    The main function.
    Runs the program.
    """
    # Initialize argparse object
    parser = argparse.ArgumentParser(description='Recieves the input and output files, in order to run the program.')
    
    # Add arguments
    parser.add_argument('-sn', '--song_name', type = str, help = 'name of the song')
    parser.add_argument('-in', '--instrument_name', type = str, help = 'name of the instrument')
    parser.add_argument('-p', '--music_sheet', help = 'path to the music sheet file')
    parser.add_argument('-i', '--instrument_file', help = 'path to the file with the instrument')
    parser.add_argument('-o', '--output', help = 'path to the output wavefile')
    parser.add_argument('-f', '--frequency', default = 48000, type = int , help = 'frequency of output')
    
    # Parsing of the arguments
    args = parser.parse_args()
    song_name = args.song_name
    song_name = Track(args.music_sheet, args.instrument_name, args.instrument_file)
    
    # Write the output file
    waver.make_wave(song_name.get_array(), args.output, args.frequency)
    
if __name__ == '__main__':
    main()