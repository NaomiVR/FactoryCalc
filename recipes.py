from dataclasses import dataclass, field
from typing import Dict, Optional
from machines import Machine
from items import Item

@dataclass
class Recipe:
    """
    Represents a crafting recipe, detailing the inputs required to produce a specific output item.
    """
    machine: Machine
    output: Item
    ingredients: Dict[Item, int]
    time_seconds: Optional[float] = None
    ratio_raw: str = ""

    # Derived fields
    name: str = field(init=False)
    icon: str = field(init=False)

    def __post_init__(self):
        # Derive display fields from output
        self.name = self.output.name
        self.icon = self.output.icon_path

        # Use machine's processing time if not explicitly provided
        if self.time_seconds is None:
            self.time_seconds = self.machine.time_seconds


# Recipes ordered by province, then machine type, then alphabetically by output name

### Valley IV ###
# Refining Unit


# Shredding Unit


# Fitting Unit


# Moulding Unit


# Seed Picking Unit


# Planting Unit


# Gearing Unit


# Filling Unit


# Packaging Unit


# Grinding Unit



### Wuling ###
# Refining Unit


# Shredding Unit


# Seed Picking Unit


# Planting Unit


# Gearing Unit


# Filling Unit


# Packaging Unit


# Grinding Unit


# Forge of the Sky


# Reactor Crucible









