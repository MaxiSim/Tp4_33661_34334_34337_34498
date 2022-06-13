import argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', type=str, help='name of someone to salute')
    parser.add_argument('-t', dest= 'repetitions', type=int, help='times to salute')
    args = parser.parse_args()
    for i in range(args.repetitions):
        print(f'Hola {args.name}')

    print(np.random.random())
    

if __name__ == '__main__':
    main()