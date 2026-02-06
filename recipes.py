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

###################################################### Valley IV ######################################################
### Refining Unit ###
amethyst_fiber_recipe_1 = Recipe(
    machine=machines.refining_unit,
    output={items.amethyst_fiber: 1},
    ingredients={items.amethyst_ore: 1},
)

amethyst_fiber_recipe_2 = Recipe(
    machine=machines.refining_unit,
    output={items.amethyst_fiber: 1},
    ingredients={items.amethyst_powder: 1},
)

carbon_powder_recipe_1 = Recipe(
    machine=machines.refining_unit,
    output={items.carbon_powder: 1},
    ingredients={items.buckflower_powder: 1},
)

carbon_powder_recipe_2 = Recipe(
    machine=machines.refining_unit,
    output={items.carbon_powder: 1},
    ingredients={items.citrome_powder: 1},
)

carbon_powder_recipe_3 = Recipe(
    machine=machines.refining_unit,
    output={items.carbon_powder: 2},
    ingredients={items.sandleaf_powder: 3},
)

carbon_recipe_1 = Recipe(
    machine=machines.refining_unit,
    output={items.carbon: 1},
    ingredients={items.buckflower: 1},
)

carbon_recipe_2 = Recipe(
    machine=machines.refining_unit,
    output={items.carbon: 1},
    ingredients={items.citrome: 1},
)

carbon_recipe_3 = Recipe(
    machine=machines.refining_unit,
    output={items.carbon: 1},
    ingredients={items.sandleaf: 1},
)

carbon_recipe_4 = Recipe(
    machine=machines.refining_unit,
    output={items.carbon: 1},
    ingredients={items.wood: 1},
)

cryston_fiber_recipe = Recipe(
    machine=machines.refining_unit,
    output={items.cryston_fiber: 1},
    ingredients={items.cryston_powder: 1},
)

dense_carbon_powder_recipe_1 = Recipe(
    machine=machines.refining_unit,
    output={items.dense_carbon_powder: 1},
    ingredients={items.ground_buckflower_powder: 1},
)

dense_carbon_powder_recipe_2 = Recipe(
    machine=machines.refining_unit,
    output={items.dense_carbon_powder: 1},
    ingredients={items.ground_citrome_powder: 1},
)

dense_origocrust_powder_recipe_2 = Recipe(
    machine=machines.refining_unit,
    output={items.dense_origocrust_powder: 1},
    ingredients={items.dense_originium_powder: 1},
)

ferrium_recipe_1 = Recipe(
    machine=machines.refining_unit,
    output={items.ferrium: 1},
    ingredients={items.ferrium_ore: 1},
)

ferrium_recipe_2 = Recipe(
    machine=machines.refining_unit,
    output={items.ferrium: 1},
    ingredients={items.ferrium_powder: 1},
)

origocrust_powder_recipe_2 = Recipe(
    machine=machines.refining_unit,
    output={items.origocrust_powder: 1},
    ingredients={items.originium_powder: 1},
)

origocrust_recipe = Recipe(
    machine=machines.refining_unit,
    output={items.origocrust: 1},
    ingredients={items.originium_ore: 1},
)

packed_origocrust_recipe = Recipe(
    machine=machines.refining_unit,
    output={items.packed_origocrust: 1},
    ingredients={items.dense_origocrust_powder: 1},
)

steel_recipe = Recipe(
    machine=machines.refining_unit,
    output={items.steel: 1},
    ingredients={items.dense_ferrium_powder: 1},
)

### Shredding Unit ###
amethyst_powder_recipe = Recipe(
    machine=machines.shredding_unit,
    output={items.amethyst_powder: 1},
    ingredients={items.amethyst_fiber: 1},
)

buckflower_powder_recipe = Recipe(
    machine=machines.shredding_unit,
    output={items.buckflower_powder: 2},
    ingredients={items.buckflower: 1},
)

citrome_powder_recipe = Recipe(
    machine=machines.shredding_unit,
    output={items.citrome_powder: 2},
    ingredients={items.citrome: 1},
)

ferry_powder_recipe = Recipe(
    machine=machines.shredding_unit,
    output={items.ferrium_powder: 1},
    ingredients={items.ferrium_ore: 1},
)

origocrust_powder_recipe_1 = Recipe(
    machine=machines.shredding_unit,
    output={items.origocrust_powder: 1},
    ingredients={items.origocrust: 1},
)

originium_powder_recipe = Recipe(
    machine=machines.shredding_unit,
    output={items.originium_powder: 1},
    ingredients={items.originium_ore: 1},
)

sandleaf_powder_recipe = Recipe(
    machine=machines.shredding_unit,
    output={items.sandleaf_powder: 3},
    ingredients={items.sandleaf: 1},
)

### Fitting Unit ###
amethyst_part_recipe = Recipe(
    machine=machines.fitting_unit,
    output={items.amethyst_part: 1},
    ingredients={items.amethyst_fiber: 1},
)

cryston_part_recipe = Recipe(
    machine=machines.fitting_unit,
    output={items.cryston_part: 1},
    ingredients={items.cryston_fiber: 1},
)

ferrium_part_recipe = Recipe(
    machine=machines.fitting_unit,
    output={items.ferrium_part: 1},
    ingredients={items.ferrium: 1},
)

steel_part_recipe = Recipe(
    machine=machines.fitting_unit,
    output={items.steel_part: 1},
    ingredients={items.steel: 1},
)

### Moulding Unit ###
amethyst_bottle_recipe_1 = Recipe(
    machine=machines.moulding_unit,
    output={items.amethyst_bottle: 1},
    ingredients={items.amethyst_fiber: 1},
)

cryston_bottle_recipe_1 = Recipe(
    machine=machines.moulding_unit,
    output={items.cryston_bottle: 1},
    ingredients={items.cryston_fiber: 1},
)

ferrium_bottle_recipe_1 = Recipe(
    machine=machines.moulding_unit,
    output={items.ferrium_bottle: 1},
    ingredients={items.ferrium: 1},
)

steel_bottle_recipe_1 = Recipe(
    machine=machines.moulding_unit,
    output={items.steel_bottle: 1},
    ingredients={items.steel: 1},
)

### Seed Picking Unit ###
aketine_seed_recipe = Recipe(
    machine=machines.seed_picking_unit,
    output={items.aketine_seed: 2},
    ingredients={items.aketine: 1},
)

buckflower_seed_recipe = Recipe(
    machine=machines.seed_picking_unit,
    output={items.buckflower_seed: 2},
    ingredients={items.buckflower: 1},
)

citrome_seed_recipe = Recipe(
    machine=machines.seed_picking_unit,
    output={items.citrome_seed: 2},
    ingredients={items.citrome: 1},
)

reed_rye_seed_recipe = Recipe(
    machine=machines.seed_picking_unit,
    output={items.reed_rye_seed: 2},
    ingredients={items.reed_rye: 1},
)

sandleaf_seed_recipe = Recipe(
    machine=machines.seed_picking_unit,
    output={items.sandleaf_seed: 2},
    ingredients={items.sandleaf: 1},
)

tartpepper_seed_recipe = Recipe(
    machine=machines.seed_picking_unit,
    output={items.tartpepper_seed: 2},
    ingredients={items.tartpepper: 1},
)

### Planting Unit ###
aketine_recipe = Recipe(
    machine=machines.planting_unit,
    output={items.aketine: 1},
    ingredients={items.aketine_seed: 1},
)

buckflower_recipe = Recipe(
    machine=machines.planting_unit,
    output={items.buckflower: 1},
    ingredients={items.buckflower_seed: 1},
)

citrome_recipe = Recipe(
    machine=machines.planting_unit,
    output={items.citrome: 1},
    ingredients={items.citrome_seed: 1},
)

sandleaf_recipe = Recipe(
    machine=machines.planting_unit,
    output={items.sandleaf: 1},
    ingredients={items.sandleaf_seed: 1},
)

### Gearing Unit ###
amethyst_component_recipe = Recipe(
    machine=machines.gearing_unit,
    output={items.amethyst_component: 1},
    ingredients={items.origocrust: 5, items.amethyst_fiber: 5},
)

cryston_component_recipe = Recipe(
    machine=machines.gearing_unit,
    output={items.cryston_component: 1},
    ingredients={items.packed_origocrust: 10, items.cryston_fiber: 10},
)

ferrium_component_recipe = Recipe(
    machine=machines.gearing_unit,
    output={items.ferrium_component: 1},
    ingredients={items.origocrust: 10, items.ferrium: 10},
)

### Filling Unit ###
buck_capsule_a_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.buck_capsule_a: 1},
    ingredients={items.steel_bottle: 10, items.ground_buckflower_powder: 10},
)

buck_capsule_b_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.buck_capsule_b: 1},
    ingredients={items.ferrium_bottle: 10, items.buckflower_powder: 10},
)

buck_capsule_c_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.buck_capsule_c: 1},
    ingredients={items.amethyst_bottle: 5, items.buckflower_powder: 5},
)

citrome_capsule_a_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.citrome_capsule_a: 1},
    ingredients={items.steel_bottle: 10, items.ground_citrome_powder: 10},
)

citrome_capsule_b_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.citrome_capsule_b: 1},
    ingredients={items.ferrium_bottle: 10, items.citrome_powder: 10},
)

citrome_capsule_c_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.citrome_capsule_c: 1},
    ingredients={items.amethyst_bottle: 5, items.citrome_powder: 5},
)

### Packaging Unit ###
hc_valley_battery_recipe = Recipe(
    machine=machines.packaging_unit,
    output={items.hc_valley_battery: 1},
    ingredients={items.steel_part: 10, items.dense_originium_powder: 15}
)

industrial_explosive_recipe = Recipe(
    machine=machines.packaging_unit,
    output={items.industrial_explosive: 1},
    ingredients={items.amethyst_part: 5, items.aketine_powder: 1}
)

lc_valley_battery_recipe = Recipe(
    machine=machines.packaging_unit,
    output={items.lc_valley_battery: 1},
    ingredients={items.amethyst_part: 5, items.originium_powder: 10}
)

sc_valley_battery_recipe = Recipe(
    machine=machines.packaging_unit,
    output={items.sc_valley_battery: 1},
    ingredients={items.ferrium_part: 10, items.originium_powder: 15}
)

### Grinding Unit ###
cryston_powder_recipe = Recipe(
    machine=machines.grinding_unit,
    output={items.cryston_powder: 1},
    ingredients={items.amethyst_powder: 2, items.sandleaf_powder: 1},
)

dense_ferrium_powder_recipe = Recipe(
    machine=machines.grinding_unit,
    output={items.dense_ferrium_powder: 1},
    ingredients={items.ferrium_powder: 2, items.sandleaf_powder: 1},
)

dense_originium_powder_recipe = Recipe(
    machine=machines.grinding_unit,
    output={items.dense_originium_powder: 1},
    ingredients={items.originium_powder: 2, items.sandleaf_powder: 1},
)

dense_origocrust_powder_recipe_1 = Recipe(
    machine=machines.grinding_unit,
    output={items.dense_origocrust_powder: 1},
    ingredients={items.origocrust_powder: 2, items.sandleaf_powder: 1},
)

ground_buckflower_powder_recipe = Recipe(
    machine=machines.grinding_unit,
    output={items.ground_buckflower_powder: 1},
    ingredients={items.buckflower_powder: 2, items.sandleaf_powder: 1},
)

ground_citrome_powder_recipe = Recipe(
    machine=machines.grinding_unit,
    output={items.ground_citrome_powder: 1},
    ingredients={items.citrome_powder: 2, items.sandleaf_powder: 1},
)


######################################################## Wuling ########################################################
### Refining Unit ###
carbon_recipe_5 = Recipe(
    machine=machines.refining_unit,
    output={items.carbon: 2},
    ingredients={items.yazhen: 1},
)

carbon_recipe_6 = Recipe(
    machine=machines.refining_unit,
    output={items.carbon: 2},
    ingredients={items.jincao: 1},
)

carbon_powder_recipe_4 = Recipe(
    machine=machines.refining_unit,
    output={items.carbon_powder: 2},
    ingredients={items.yazhen_powder: 1},
)

carbon_powder_recipe_5 = Recipe(
    machine=machines.refining_unit,
    output={items.carbon_powder: 2},
    ingredients={items.jincao_powder: 1},
)

stabilized_carbon_recipe = Recipe(
    machine=machines.refining_unit,
    output={items.stabilized_carbon: 1},
    ingredients={items.dense_carbon_powder: 1},
)

### Shredding Unit ###
carbon_powder_recipe_6 = Recipe(
    machine=machines.shredding_unit,
    output={items.carbon_powder: 2},
    ingredients={items.carbon_powder: 1},
)

jincao_powder_recipe = Recipe(
    machine=machines.shredding_unit,
    output={items.jincao_powder: 2},
    ingredients={items.jincao_solution: 1},
)

yazhen_powder_recipe = Recipe(
    machine=machines.shredding_unit,
    output={items.yazhen_powder: 2},
    ingredients={items.yazhen_solution: 1},
)

### Seed Picking Unit ###
amber_rice_seed_recipe = Recipe(
    machine=machines.seed_picking_unit,
    output={items.amber_rice_seed: 2},
    ingredients={items.amber_rice: 1},
)

jincao_seed_recipe = Recipe(
    machine=machines.seed_picking_unit,
    output={items.jincao_seed: 1},
    ingredients={items.jincao: 1},
)

redjade_ginseng_seed_recipe = Recipe(
    machine=machines.seed_picking_unit,
    output={items.redjade_ginseng_seed: 2},
    ingredients={items.redjade_ginseng: 1},
)

yazhen_seed_recipe = Recipe(
    machine=machines.seed_picking_unit,
    output={items.yazhen_seed: 1},
    ingredients={items.yazhen: 1},
)

### Planting Unit ###
jincao_recipe = Recipe(
    machine=machines.planting_unit,
    output={items.jincao: 2},
    ingredients={items.jincao_seed: 1, items.clean_water: 1},
)

yazhen_recipe = Recipe(
    machine=machines.planting_unit,
    output={items.yazhen: 2},
    ingredients={items.yazhen_seed: 1, items.clean_water: 1},
)

### Gearing Unit ###
xiranite_component_recipe = Recipe(
    machine=machines.gearing_unit,
    output={items.xiranite_component: 1},
    ingredients={items.packed_origocrust: 10, items.xiranite: 10},
)

### Filling Unit ###
amethyst_bottled_yazhen_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.amethyst_bottle_yazhen: 1},
    ingredients={items.amethyst_bottle: 1, items.yazhen_solution: 1},
)

amethyst_bottled_jincao_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.amethyst_bottle_jincao: 1},
    ingredients={items.amethyst_bottle: 1, items.jincao_solution: 1},
)

amethyst_bottled_clean_water_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.amethyst_bottle_clean_water: 1},
    ingredients={items.amethyst_bottle: 1, items.clean_water: 1},
)

amethyst_bottled_liquid_xiranite_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.amethyst_bottle_liquid_xiranite: 1},
    ingredients={items.amethyst_bottle: 1, items.liquid_xiranite: 1},
)

cryston_bottled_yazhen_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.cryston_bottle_yazhen: 1},
    ingredients={items.cryston_bottle: 1, items.yazhen_solution: 1},
)

cryston_bottled_jincao_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.cryston_bottle_jincao: 1},
    ingredients={items.cryston_bottle: 1, items.jincao_solution: 1},
)

cryston_bottled_clean_water_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.cryston_bottle_clean_water: 1},
    ingredients={items.cryston_bottle: 1, items.clean_water: 1},
)

cryston_bottled_liquid_xiranite_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.cryston_bottle_liquid_xiranite: 1},
    ingredients={items.cryston_bottle: 1, items.liquid_xiranite: 1},
)

ferrium_bottled_yazhen_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.ferrium_bottle_yazhen: 1},
    ingredients={items.ferrium_bottle: 1, items.yazhen_solution: 1},
)

ferrium_bottled_jincao_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.ferrium_bottle_jincao: 1},
    ingredients={items.ferrium_bottle: 1, items.jincao_solution: 1},
)

ferrium_bottled_clean_water_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.ferrium_bottle_clean_water: 1},
    ingredients={items.ferrium_bottle: 1, items.clean_water: 1},
)

ferrium_bottled_liquid_xiranite_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.ferrium_bottle_liquid_xiranite: 1},
    ingredients={items.ferrium_bottle: 1, items.liquid_xiranite: 1},
)

steel_bottled_yazhen_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.steel_bottle_yazhen: 1},
    ingredients={items.steel_bottle: 1, items.yazhen_solution: 1},
)

steel_bottled_jincao_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.steel_bottle_jincao: 1},
    ingredients={items.steel_bottle: 1, items.jincao_solution: 1},
)

steel_bottled_clean_water_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.steel_bottle_clean_water: 1},
    ingredients={items.steel_bottle: 1, items.clean_water: 1},
)

steel_bottled_liquid_xiranite_recipe = Recipe(
    machine=machines.filling_unit,
    output={items.steel_bottle_liquid_xiranite: 1},
    ingredients={items.steel_bottle: 1, items.liquid_xiranite: 1},
)

### Separating Unit ###


### Packaging Unit ###
jincao_drink_recipe = Recipe(
    machine=machines.packaging_unit,
    output={items.jincao_drink: 1},
    ingredients={items.ferrium_part: 10, items.ferrium_bottle_jincao: 5},
)

lc_wuling_battery_recipe = Recipe(
    machine=machines.packaging_unit,
    output={items.lc_wuling_battery: 1},
    ingredients={items.xiranite: 5, items.dense_originium_powder: 15},
)

yazhen_syringe_c_recipe = Recipe(
    machine=machines.packaging_unit,
    output={items.yazhen_syringe_c: 1},
    ingredients={items.ferrium_part: 10, items.ferrium_bottle_yazhen: 5},
)

### Grinding Unit ###
dense_carbon_powder_recipe_3 = Recipe(
    machine=machines.grinding_unit,
    output={items.dense_carbon_powder: 1},
    ingredients={items.carbon_powder: 2, items.sandleaf_powder: 1},
)

### Forge of the Sky ###
xiranite_recipe = Recipe(
    machine=machines.forge_of_the_sky,
    output={items.xiranite: 1},
    ingredients={items.stabilized_carbon: 2, items.clean_water: 1},
)

### Reactor Crucible ###
jincao_solution_recipe = Recipe(
    machine=machines.reactor_crucible,
    output={items.jincao_solution: 1},
    ingredients={items.jincao_powder: 1, items.clean_water: 1},
)

liquid_xiranite_recipe = Recipe(
    machine=machines.reactor_crucible,
    output={items.liquid_xiranite: 1},
    ingredients={items.xiranite: 1, items.clean_water: 1},
)

yazhen_solution_recipe = Recipe(
    machine=machines.reactor_crucible,
    output={items.yazhen_solution: 1},
    ingredients={items.yazhen_powder: 1, items.clean_water: 1},
)
