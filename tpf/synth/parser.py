import argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--music_sheet', type=str, help='file with music sheet')
    parser.add_argument('-i', '--instrument', type=str, help='file with instrument')
    parser.add_argument('-o', '--output', type=str, help='wavefile with output')
    parser.add_argument('-f', '--frequency', type=int, help='frequency of output')
    args = parser.parse_args()

    print(args)

if __name__ == '__main__':
    main()