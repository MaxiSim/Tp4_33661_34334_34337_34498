"""
This module implements some useful functions as an aside for the Synthesizer project of a programming course at the
Universidad de San Andrés, Argentina.
With it, standard midi files can be converted to the type of music score that the project needs.

@author Patricio Moreno
@institution Universidad de San Andrés
@date 2022-06-09 Thu 16:30:58 -0300
"""
from notes import notes_mapping

import argparse
import math
from typing import Optional, IO

import mido


def m2f(midi_note: int, freq_la4: int = 440) -> float:
    """Convert a midi note to the corresponding frequency, based on LA4 @ 440 Hz

    Take into account that a midi note is an integer value in the range [0, 127].
    Values out of that range will give answers with no real life meaning (in MIDI field).

    Parameters
    ----------
    midi_note : int
        The number representing the midi note

    freq_la4 : int
        The frequency (in Hz) of a tuned A4, typically 440 Hz.

    Returns
    -------
        The frequency of the note ranging from about 8 Hz to 12.5 kHz
    """
    return (freq_la4 / 32) * (2 ** ((midi_note - 9) / 12))


def f2m(freq: float) -> int:
    """Convert a frequency to the corresponding midi note

    Take into account that the valid range of frequencies for a midi file is between 8 Hz and 12.5 kHz.
    Values out of that range may have no sense or raise an error (ValueError: math domain error).

    Parameters
    ----------
    freq : float
        The frequency (in Hz) to be converted

    Returns
    -------
        The corresponding midi note
    """
    return 69 + round(12 * math.log2(freq / 440))


def freq2cypher(frequency: float, notes: dict[str, float]) -> Optional[str]:
    """Convert a frequency to the corresponding cypher in english notation.

    Parameters
    ----------
    frequency : float
        The frequency to convert, in Hz.

    note : dict[str, float]
        A mapping from english notation to frequency and viceversa.

    Returns
    -------
        The frequency represented using english notation (for an approximate value of the frequency) or None
    """
    for note, f in notes:
        if f - 1 < frequency < f + 1:
            return note
    return None


def convert_midi(ofile: str, midifile: str, tracks: Optional[list[int]] = None) -> None:
    """Convert desired tracks of a midi file to a common text-based score

    Parameters
    ----------
    ofile : str
        The path to the output (text) file

    midi_file : str
        The path to the input midi file

    tracks : list[int] or None
        If supplied, it should hold the numbers of the tracks to convert

    Returns
    -------
        Nothing
    """
    midi = mido.MidiFile(midifile)
    if tracks is None or tracks == []:
        tracks = list(range(len(midi.tracks)))
    with open(ofile, 'wt') as output:
        playing = {}
        t = 0
        for msg in midi:
            t += msg.time
            if msg.is_meta:
                pass
            elif msg.type == 'note_on' and msg.channel in tracks:
                freq = m2f(msg.note)
                score = freq2cypher(freq, notes_mapping)
                if score is None:
                    score = (None, freq)
                playing[msg.note] = (t, score)
            elif msg.type == 'note_off' and msg.channel in tracks:
                start, note = playing[msg.note]
                output.write(f"{start} {note} {t - start}\n")


def load_midi(filepath: str) -> IO:
    """Load a midifile into a MidiFile object

    Parameters
    ----------
    filepath : str
        The path to the input midi file

    Returns
    -------
        The MidiFile object
    """
    return mido.MidiFile(filepath)


def main() -> None:
    parser = argparse.ArgumentParser(description='Conversor de MIDI')
    parser.add_argument('-i', '--input', help='archivo MIDI')
    parser.add_argument('-o', '--output', help='archivo de salida')
    parser.add_argument('-t', '--tracks', help='tracks a convertir (CSV)')

    # ------------------------------------------------------------------
    # Parseo de argumentos
    # ------------------------------------------------------------------
    arg = parser.parse_args()

    if arg.tracks is not None:
        tracks = arg.tracks.replace(" ", "").split(",")
    else:
        tracks = None

    convert_midi(arg.output, arg.input, tracks)


if __name__ == '__main__':
    main()
