from dataclasses import dataclass
from machines import Machine
from items import Item

@dataclass
class Recipe:
    """
    Represents a crafting recipe, detailing the inputs required to produce a specific output item.
    """

    name: str
    icon: str
    machine: Machine
    output: Item
    ingredients: dict[Item, int]  # Mapping of Item to quantity required
    time_seconds: float
    ratio_raw: str # Used for GUI display
    
    
    
    def __post_init__(self):
        """
        Logic to automatically assign the icon based on the recipe's output.
        """
        self.name = self.output.name
        self.icon_path = self.output.icon_path


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









