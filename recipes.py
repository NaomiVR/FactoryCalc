from dataclasses import dataclass
from typing import Dict, Optional, List
from items import Item, ITEM_REGISTRY
from machines import Machine, MACHINE_REGISTRY



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
    machine: Machine
    output: Dict[Item, int]
    ingredients: Dict[Item, int]
    time_seconds: Optional[float] = None
    ratio_raw: str = ""

    def __post_init__(self) -> None:
        self._type_checks()
        self._validate_inputs()
        self._resolve_timing()

    def _type_checks(self) -> None:
        """Basic type checks"""
        if not isinstance(self.machine, Machine):
            raise TypeError(f"Machine must be a machines.Machine instance, got {type(self.machine)}")
        if not isinstance(self.output, dict) or not isinstance(self.ingredients, dict):
            raise TypeError("Output and ingredients must be dicts mapping items.Item -> int")
        if not self.output:
            raise ValueError("Recipe.output must contain at least one item.")

    def _validate_inputs(self) -> None:
        """Validate keys/values in output and ingredients"""
        for k, v in self.output.items():
            if not isinstance(k, Item):
                raise TypeError(f"Output keys must be items.Item instances, got {type(k)!r}")
            if not isinstance(v, int) or v <= 0:
                raise ValueError(f"Output quantities must be positive ints, got {v!r} for {k.name}")

        for k, v in self.ingredients.items():
            if not isinstance(k, Item):
                raise TypeError(f"Ingredient keys must be items.Item instances, got {type(k)!r}")
            if not isinstance(v, int) or v <= 0:
                raise ValueError(f"Ingredient quantities must be positive ints, got {v!r} for {k.name}")

    def _resolve_timing(self) -> None:
        """Determine processing time: prefer explicit recipe value, fallback to machine"""
        if self.time_seconds is None:
            self.time_seconds = getattr(self.machine, "time_seconds", None)
        if self.time_seconds is None:
            raise ValueError("time_seconds was not provided and machine has no 'time_seconds' attribute")
        if self.time_seconds <= 0:
            raise ValueError("time_seconds must be positive")

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


class RecipeManager:
    @staticmethod
    def load_from_definitions(definitions, item_reg, mach_reg) -> List[Recipe]:
        recipes = []
        for m_name, outputs, inputs in definitions:
            try:
                recipes.append(Recipe(
                    machine=mach_reg[m_name],
                    output={item_reg[name]: qty for name, qty in outputs.items()},
                    ingredients={item_reg[name]: qty for name, qty in inputs.items()}
                ))
            except KeyError as e:
                print(f"Error loading recipe: Missing key {e}")
        return recipes


# Recipes ordered by province, then machine type, then alphabetically by output name

# Format: (machine_name, {output_item_name: quantity}, {ingredient_item_name: quantity}),
# Example: ("refining_unit", {"amethyst_fiber": 1}, {"amethyst_ore": 1}),
# or ("fitting_unit", {"amethyst_part": 1}, {"amethyst_fiber": 1, "carbon": 1}),
# Add all recipes here in a structured format, then instantiate them in bulk to avoid manual errors and improve maintainability.
RECIPE_DEFINITIONS = [
    #################################################### Valley IV ####################################################
    ### Refining Unit ###
    ("refining_unit", {"amethyst_fiber": 1}, {"amethyst_ore": 1}),
    ("refining_unit", {"amethyst_fiber": 1}, {"amethyst_powder": 1}),
    ("refining_unit", {"carbon_powder": 1}, {"buckflower_powder": 1}),
    ("refining_unit", {"carbon_powder": 1}, {"citrome_powder": 1}),
    ("refining_unit", {"carbon_powder": 2}, {"sandleaf_powder": 3}),
    ("refining_unit", {"carbon": 1}, {"buckflower": 1}),
    ("refining_unit", {"carbon": 1}, {"citrome": 1}),
    ("refining_unit", {"carbon": 1}, {"sandleaf": 1}),
    ("refining_unit", {"carbon": 1}, {"wood": 1}),
    ("refining_unit", {"cryston_fiber": 1}, {"cryston_powder": 1}),
    ("refining_unit", {"dense_carbon_powder": 1}, {"ground_buckflower_powder": 1}),
    ("refining_unit", {"dense_carbon_powder": 1}, {"ground_citrome_powder": 1}),
    ("refining_unit", {"dense_origocrust_powder": 1}, {"dense_originium_powder": 1}),
    ("refining_unit", {"ferrium": 1}, {"ferrium_ore": 1}),
    ("refining_unit", {"ferrium": 1}, {"ferrium_powder": 1}),
    ("refining_unit", {"origocrust_powder": 1}, {"originium_powder": 1}),
    ("refining_unit", {"origocrust": 1}, {"originium_ore": 1}),
    ("refining_unit", {"packed_origocrust": 1}, {"dense_origocrust_powder": 1}),
    ("refining_unit", {"steel": 1}, {"dense_ferrium_powder": 1}),

    ### Shredding Unit ###
    ("shredding_unit", {"amethyst_powder": 1}, {"amethyst_fiber": 1}),
    ("shredding_unit", {"buckflower_powder": 2}, {"buckflower": 1}),
    ("shredding_unit", {"citrome_powder": 2}, {"citrome": 1}),
    ("shredding_unit", {"ferrium_powder": 1}, {"ferrium_ore": 1}),
    ("shredding_unit", {"origocrust_powder": 1}, {"origocrust": 1}),
    ("shredding_unit", {"originium_powder": 1}, {"originium_ore": 1}),
    ("shredding_unit", {"sandleaf_powder": 3}, {"sandleaf": 1}),

    ### Fitting Unit ###
    ("fitting_unit", {"amethyst_part": 1}, {"amethyst_fiber": 1}),
    ("fitting_unit", {"cryston_part": 1}, {"cryston_fiber": 1}),
    ("fitting_unit", {"ferrium_part": 1}, {"ferrium": 1}),
    ("fitting_unit", {"steel_part": 1}, {"steel": 1}),

    ### Moulding Unit ###
    ("moulding_unit", {"amethyst_bottle": 1}, {"amethyst_fiber": 1}),
    ("moulding_unit", {"cryston_bottle": 1}, {"cryston_fiber": 1}),
    ("moulding_unit", {"ferrium_bottle": 1}, {"ferrium": 1}),
    ("moulding_unit", {"steel_bottle": 1}, {"steel": 1}),

    ### Seed Picking Unit ###
    ("seed_picking_unit", {"aketine_seed": 2}, {"aketine": 1}),
    ("seed_picking_unit", {"buckflower_seed": 2}, {"buckflower": 1}),
    ("seed_picking_unit", {"citrome_seed": 2}, {"citrome": 1}),
    ("seed_picking_unit", {"reed_rye_seed": 2}, {"reed_rye": 1}),
    ("seed_picking_unit", {"sandleaf_seed": 2}, {"sandleaf": 1}),
    ("seed_picking_unit", {"tartpepper_seed": 2}, {"tartpepper": 1}),

    ### Planting Unit ###
    ("planting_unit", {"aketine": 1}, {"aketine_seed": 1}),
    ("planting_unit", {"buckflower": 1}, {"buckflower_seed": 1}),
    ("planting_unit", {"citrome": 1}, {"citrome_seed": 1}),
    ("planting_unit", {"sandleaf": 1}, {"sandleaf_seed": 1}),

    ### Gearing Unit ###
    ("gearing_unit", {"amethyst_component": 1}, {"origocrust": 5, "amethyst_fiber": 5}),
    ("gearing_unit", {"cryston_component": 1}, {"packed_origocrust": 10, "cryston_fiber": 10}),
    ("gearing_unit", {"ferrium_component": 1}, {"origocrust": 10, "ferrium": 10}),

    ### Filling Unit ###
    ("filling_unit", {"buck_capsule_a": 1}, {"steel_bottle": 10, "ground_buckflower_powder": 10}),
    ("filling_unit", {"buck_capsule_b": 1}, {"ferrium_bottle": 10, "buckflower_powder": 10}),
    ("filling_unit", {"buck_capsule_c": 1}, {"amethyst_bottle": 5, "buckflower_powder": 5}),
    ("filling_unit", {"citrome_capsule_a": 1}, {"steel_bottle": 10, "ground_citrome_powder": 10}),
    ("filling_unit", {"citrome_capsule_b": 1}, {"ferrium_bottle": 10, "citrome_powder": 10}),
    ("filling_unit", {"citrome_capsule_c": 1}, {"amethyst_bottle": 5, "citrome_powder": 5}),

    ### Packaging Unit ###
    ("packaging_unit", {"hc_valley_battery": 1}, {"steel_part": 10, "dense_originium_powder": 15}),
    ("packaging_unit", {"industrial_explosive": 1}, {"amethyst_part": 5, "aketine_powder": 1}),
    ("packaging_unit", {"lc_valley_battery": 1}, {"amethyst_part": 5, "originium_powder": 10}),
    ("packaging_unit", {"sc_valley_battery": 1}, {"ferrium_part": 10, "originium_powder": 15}),

    ### Grinding Unit ###
    ("grinding_unit", {"cryston_powder": 1}, {"amethyst_powder": 2, "sandleaf_powder": 1}),
    ("grinding_unit", {"dense_ferrium_powder": 1}, {"ferrium_powder": 2, "sandleaf_powder": 1}),
    ("grinding_unit", {"dense_originium_powder": 1}, {"originium_powder": 2, "sandleaf_powder": 1}),
    ("grinding_unit", {"dense_origocrust_powder": 1}, {"origocrust_powder": 2, "sandleaf_powder": 1}),
    ("grinding_unit", {"ground_buckflower_powder": 1}, {"buckflower_powder": 2, "sandleaf_powder": 1}),
    ("grinding_unit", {"ground_citrome_powder": 1}, {"citrome_powder": 2, "sandleaf_powder": 1}),

    ###################################################### Wuling ######################################################
    ### Refining Unit ###
    ("refining_unit", {"carbon": 2}, {"yazhen": 1}),
    ("refining_unit", {"carbon": 2}, {"jincao": 1}),
    ("refining_unit", {"carbon_powder": 2}, {"yazhen_powder": 1}),
    ("refining_unit", {"carbon_powder": 2}, {"jincao_powder": 1}),
    ("refining_unit", {"stabilized_carbon": 1}, {"dense_carbon_powder": 1}),

    ### Shredding Unit ###
    ("shredding_unit", {"carbon_powder": 2}, {"carbon_powder": 1}),
    ("shredding_unit", {"jincao_powder": 2}, {"jincao_solution": 1}),
    ("shredding_unit", {"yazhen_powder": 2}, {"yazhen_solution": 1}),

    ### Seed Picking Unit ###
    ("seed_picking_unit", {"amber_rice_seed": 2}, {"amber_rice": 1}),
    ("seed_picking_unit", {"jincao_seed": 1}, {"jincao": 1}),
    ("seed_picking_unit", {"redjade_ginseng_seed": 2}, {"redjade_ginseng": 1}),
    ("seed_picking_unit", {"yazhen_seed": 1}, {"yazhen": 1}),

    ### Planting Unit ###
    ("planting_unit_wuling", {"jincao": 2}, {"jincao_seed": 1, "clean_water": 1}),
    ("planting_unit_wuling", {"yazhen": 2}, {"yazhen_seed": 1, "clean_water": 1}),

    ### Gearing Unit ###
    ("gearing_unit", {"xiranite_component": 1}, {"packed_origocrust": 10, "xiranite": 10}),

    ### Filling Unit ###
    ("filling_unit", {"amethyst_bottle_yazhen": 1}, {"amethyst_bottle": 1, "yazhen_solution": 1}),
    ("filling_unit", {"amethyst_bottle_jincao": 1}, {"amethyst_bottle": 1, "jincao_solution": 1}),
    ("filling_unit", {"amethyst_bottle_clean_water": 1}, {"amethyst_bottle": 1, "clean_water": 1}),
    ("filling_unit", {"amethyst_bottle_liquid_xiranite": 1}, {"amethyst_bottle": 1, "liquid_xiranite": 1}),
    ("filling_unit", {"cryston_bottle_yazhen": 1}, {"cryston_bottle": 1, "yazhen_solution": 1}),
    ("filling_unit", {"cryston_bottle_jincao": 1}, {"cryston_bottle": 1, "jincao_solution": 1}),
    ("filling_unit", {"cryston_bottle_clean_water": 1}, {"cryston_bottle": 1, "clean_water": 1}),
    ("filling_unit", {"cryston_bottle_liquid_xiranite": 1}, {"cryston_bottle": 1, "liquid_xiranite": 1}),
    ("filling_unit", {"ferrium_bottle_yazhen": 1}, {"ferrium_bottle": 1, "yazhen_solution": 1}),
    ("filling_unit", {"ferrium_bottle_jincao": 1}, {"ferrium_bottle": 1, "jincao_solution": 1}),
    ("filling_unit", {"ferrium_bottle_clean_water": 1}, {"ferrium_bottle": 1, "clean_water": 1}),
    ("filling_unit", {"ferrium_bottle_liquid_xiranite": 1}, {"ferrium_bottle": 1, "liquid_xiranite": 1}),
    ("filling_unit", {"steel_bottle_yazhen": 1}, {"steel_bottle": 1, "yazhen_solution": 1}),
    ("filling_unit", {"steel_bottle_jincao": 1}, {"steel_bottle": 1, "jincao_solution": 1}),
    ("filling_unit", {"steel_bottle_clean_water": 1}, {"steel_bottle": 1, "clean_water": 1}),
    ("filling_unit", {"steel_bottle_liquid_xiranite": 1}, {"steel_bottle": 1, "liquid_xiranite": 1}),

    ### Separating Unit ###
    ("separating_unit", {"amethyst_bottle": 1, "yazhen_solution": 1}, {"amethyst_bottle_yazhen": 1}),
    ("separating_unit", {"amethyst_bottle": 1, "jincao_solution": 1}, {"amethyst_bottle_jincao": 1}),
    ("separating_unit", {"amethyst_bottle": 1, "clean_water": 1}, {"amethyst_bottle_clean_water": 1}),
    ("separating_unit", {"amethyst_bottle": 1, "liquid_xiranite": 1}, {"amethyst_bottle_liquid_xiranite": 1}),
    ("separating_unit", {"cryston_bottle": 1, "yazhen_solution": 1}, {"cryston_bottle_yazhen": 1}),
    ("separating_unit", {"cryston_bottle": 1, "jincao_solution": 1}, {"cryston_bottle_jincao": 1}),
    ("separating_unit", {"cryston_bottle": 1, "clean_water": 1}, {"cryston_bottle_clean_water": 1}),
    ("separating_unit", {"cryston_bottle": 1, "liquid_xiranite": 1}, {"cryston_bottle_liquid_xiranite": 1}),
    ("separating_unit", {"ferrium_bottle": 1, "yazhen_solution": 1}, {"ferrium_bottle_yazhen": 1}),
    ("separating_unit", {"ferrium_bottle": 1, "jincao_solution": 1}, {"ferrium_bottle_jincao": 1}),
    ("separating_unit", {"ferrium_bottle": 1, "clean_water": 1}, {"ferrium_bottle_clean_water": 1}),
    ("separating_unit", {"ferrium_bottle": 1, "liquid_xiranite": 1}, {"ferrium_bottle_liquid_xiranite": 1}),
    ("separating_unit", {"steel_bottle": 1, "yazhen_solution": 1}, {"steel_bottle_yazhen": 1}),
    ("separating_unit", {"steel_bottle": 1, "jincao_solution": 1}, {"steel_bottle_jincao": 1}),
    ("separating_unit", {"steel_bottle": 1, "clean_water": 1}, {"steel_bottle_clean_water": 1}),
    ("separating_unit", {"steel_bottle": 1, "liquid_xiranite": 1}, {"steel_bottle_liquid_xiranite": 1}),

    ### Packaging Unit ###
    ("packaging_unit", {"jincao_drink": 1}, {"ferrium_part": 10, "ferrium_bottle_jincao": 5}),
    ("packaging_unit", {"lc_wuling_battery": 1}, {"xiranite": 5, "dense_originium_powder": 15}),
    ("packaging_unit", {"yazhen_syringe_c": 1}, {"ferrium_part": 10, "ferrium_bottle_yazhen": 5}),

    ### Grinding Unit ###
    ("grinding_unit", {"dense_carbon_powder": 1}, {"carbon_powder": 2, "sandleaf_powder": 1}),

    ### Forge of the Sky ###
    ("forge_of_the_sky", {"xiranite": 1}, {"stabilized_carbon": 2, "clean_water": 1}),

    ### Reactor Crucible ###
    ("reactor_crucible", {"jincao_solution": 1}, {"jincao_powder": 1, "clean_water": 1}),
    ("reactor_crucible", {"liquid_xiranite": 1}, {"xiranite": 1, "clean_water": 1}),
    ("reactor_crucible", {"yazhen_solution": 1}, {"yazhen_powder": 1, "clean_water": 1}),
]

# Load all recipes from definitions into a list of Recipe objects, resolving item and machine references from the registries.
RECIPE_REGISTRY = RecipeManager.load_from_definitions(RECIPE_DEFINITIONS, ITEM_REGISTRY, MACHINE_REGISTRY)
