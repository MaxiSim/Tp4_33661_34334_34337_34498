# Tp_final

To start, the user needs to install the modules needed for the program to work. 

1) cd path/to/Tp_final

2) Install the dependencies: 
    pip install -r requirements.txt

3) Install it with pip:
    $ pip install .


-- The user will use a parser which receives different types of files and will analyze those files in order to produce a song. The files needed include:
    A text file which includes the different harmonics of an instrument, and a text file with the score of a song. 
    The first line of the instrument file will have the number of harmonics, the next lines will have the amplitude of each harmonic. The last three lines will need to have first the function for the attack of each note, then the function for sustain and at the end the function for the decay.

-- In order to use the parser and run the program:

    1) Open a terminal

    2) cd path/to/Tp_final/synth-main

    3) Run the program:
        $ python main.py -sn "song_name" -in "instrument_name" -p scores/filename.txt -i instruments/filename.txt -o wavefiles/filename.txt 
    (-f "frequency" is optional and default is 48000, in case another frequency is needed, -f "frequency" should be the last argument)
    (python/python3 depending on the OS)

    4) The program will generate a wave file with the name "filename.wav". This file will be in the folder "wavefiles", 
    and is the one that the user will use to play the song, with a wave player.

Xylophone:
-- In order to communicate with the real xylophone:

    1) Open a terminal

    2) cd path/to/Tp_final/xylophone-main/main

    3) Run the program:
        $ python3 main_server.py

    4) Open a new terminal window 
    
    5) cd path/to/Tp_final/xylophone-main/main

    6) Run the program:
        $ python3 main_client.py -p scores/filename.txt
    
    (python main_mock_server.py can be used to test the client)

