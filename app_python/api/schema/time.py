"""
This module contains the schema of the current time in Moscow.
"""


class TimeSchema():
    """
    This class represents the schema of the current time in Moscow.
    """
    description = 'The current time in Moscow: '
    type = 'string'
    format = 'time'

    def dump(self, obj):
        """
        Returns the current time in Moscow.

        Args:
            obj (TimeModel): The current time in Moscow.

        Returns:
            str: The current time in Moscow in the format HH:MM:SS.
        """
        return self.description + obj.time.strftime("%H:%M:%S")
