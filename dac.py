"""Module containing the DAC class."""

from dataclasses import dataclass


@dataclass(slots=True)
class DAC:
    """Class representing a Digital-to-Analog Converter.

    Do not instantiate this class manually as it has no bounds checking,
    instead use the factory method to construct the class.
    """

    analog: float

    @property
    def digital(self) -> int:
        """The number returned from this getter and the value expected for the
        setter are expected to be a binary reresentation, e.g. `0x0110100100`.
        To print this number in a binary format, use the `0=10b` format
        in an f-string or `str.format()`."""

        return round(self.analog * 204.6)

    @digital.setter
    def digital(self, value: int) -> None:
        if value > 0b1111111111:
            raise ValueError(
                f"voltage must be between 0 and 0x1111111111 (is {value:0=10b})"
            )
        self.analog = value / 204.6


def create_dac(voltage: float) -> DAC:
    if voltage < 0 or voltage > 5:
        raise ValueError(f"voltage must be between 0 and 5 (is {voltage})")
    return DAC(voltage)
