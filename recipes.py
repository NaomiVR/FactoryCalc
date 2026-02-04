from dataclasses import dataclass
from typing import Dict, Optional
import machines
import items

@dataclass
class Recipe:
    """
    Represents a crafting recipe, detailing the inputs required to produce a specific output item.
    Attributes:
        machine (machines.Machine): The machine used to process this recipe.
        output (Dict[items.Item, int]): A dictionary mapping output items to their quantities.
        ingredients (Dict[items.Item, int]): A dictionary mapping input items to their required quantities.
        time_seconds (Optional[float]): Time in seconds to process one cycle of the recipe. If None, defaults to machine's time.
        ratio_raw (str): Raw string representation of the production ratio for display purposes.
    Derived Attributes:
        name (str): The display name of the recipe, derived from the first output item.
        icon (str): The icon path for the recipe, derived from the first output item.
    """
    machine: machines.Machine
    output: Dict[items.Item, int]
    ingredients: Dict[items.Item, int]
    time_seconds: Optional[float] = None
    ratio_raw: str = ""

    def __post_init__(self) -> None:
        self._type_checks()
        self._validate_inputs()
        self._resolve_timing()

    def _type_checks(self) -> None:
        """Basic type checks"""
        if not isinstance(self.machine, machines.Machine):
            raise TypeError(f"Machine must be a machines.Machine instance, got {type(self.machine)}")

        if not isinstance(self.output, dict) or not isinstance(self.ingredients, dict):
            raise TypeError("Output and ingredients must be dicts mapping items.Item -> int")

        if not self.output:
            raise ValueError("Recipe.output must contain at least one item.")

    def _validate_inputs(self) -> None:
        """Validate keys/values in output and ingredients"""
        for k, v in self.output.items():
            if not isinstance(k, items.Item):
                raise TypeError(f"Output keys must be items.Item instances, got {type(k)!r}")
            if not isinstance(v, int) or v <= 0:
                raise ValueError(f"Output quantities must be positive ints, got {v!r} for {k.name}")

        for k, v in self.ingredients.items():
            if not isinstance(k, items.Item):
                raise TypeError(f"Ingredient keys must be items.Item instances, got {type(k)!r}")
            if not isinstance(v, int) or v <= 0:
                raise ValueError(f"Ingredient quantities must be positive ints, got {v!r} for {k.name}")

    def _resolve_timing(self) -> None:
        """Determine processing time: prefer explicit recipe value, fallback to machine"""
        if self.time_seconds is None:
            self.time_seconds = getattr(self.machine, "time_seconds", None)
            if self.time_seconds is None:
                raise ValueError("time_seconds was not provided and machine has no 'time_seconds' attribute")

    @property
    def name(self) -> str:
        """Derived display name from the first output item"""
        first_output_item = next(iter(self.output))
        return first_output_item.name

    @property
    def icon(self) -> str:
        """Derived icon path from the first output item"""
        first_output_item = next(iter(self.output))
        return first_output_item.icon_path

    @property
    def total_output_count(self) -> int:
        """Total quantity produced per cycle (sum of output cycles)"""
        return sum(self.output.values())

    @property
    def cycles_per_minute(self) -> float:
        """How many cycles can run per minute given time_seconds for one cycle"""
        if self.time_seconds <= 0:
            return float("inf") if self.time_seconds == 0 else 0.0
        return 60.0 / self.time_seconds

    @property
    def items_per_minute(self) -> float:
        """Total items produced per minute (cycles_per_minute * total_output_count"""
        return self.cycles_per_minute * self.total_output_count


# Recipes ordered by province, then machine type, then alphabetically by output name

### Valley IV ###
# Refining Unit
origocrust_recipe = Recipe(
    machine=machines.refining_unit,
    output={items.origocrust: 1},
    ingredients={items.originium_ore: 1},
)

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









