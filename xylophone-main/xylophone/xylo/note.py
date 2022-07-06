import json
from typing import Dict

class XyloNote:
    def __init__(self, value: str, start_time: float, velocity: int) -> None:
        """Instantiates a XyloNote(value, start_time, velocity)

        Args:
            value (str): name of the note.
            start_time (float): time in which the note is played.
            velocity (int): set the velocity of the played note.

        Raises:
            ValueError: The start_time must be convertible to float
            ValueError: Velocity must be an integer.
            ValueError: Velocity must be between 0 and 127.
        """

        try:
            start_time = float(start_time)
        except (TypeError, ValueError):
            raise ValueError('The start_time must be convertible to float')

        if not isinstance(velocity, int):
            raise ValueError('Velocity must be an integer')

        if velocity < 0 and velocity > 127:
            raise ValueError('Please use a velocity between 0 and 127')

        self.value = value
        self.start_time = start_time
        self.velocity = velocity


    @staticmethod
    def from_json(json_dct: Dict):
        """Method to deserialize JSON

        Args:
            json_dct (dict): JSON to deserialize

        Returns:
            XyloNote: object instance
        """
        return XyloNote(
                json_dct['value'],
                json_dct['start_time'],
                json_dct['velocity'],
            )

    def to_json(self) -> str:
        """Serializes self"""
        return json.dumps(self, default=lambda o: o.__dict__)


    def __str__(self):
        return f'Note: {self.value} | Start time: {self.start_time} | Velocity: {self.velocity}'


    def __repr__(self):
        return f'{self.__class__}(note={self.value},start_time={self.start_time},velocity={self.velocity}'

