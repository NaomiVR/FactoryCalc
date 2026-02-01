from dataclasses import dataclass


@dataclass
class Machine:
    """
    Represents the physical machine constraints (Grid size, slots, etc.).
    """
    name: str
    size: tuple[int, int] # e.g. (3, 3) - width, height - input and output slots on width opposite sides
    physical_input_slots: int = 0
    physical_output_slots: int = 0
    liquid_input_slots: int = 0
    liquid_output_slots: int = 0
    power_usage: float = 0.0
