from dataclasses import dataclass


@dataclass
class Building:
    """
    Represents the base building and therefore base attributes, name and size
    """
    name: str
    size: tuple[int, int]  # e.g. (3, 3) - width, height
    description: str
    on_ground: bool = True


@dataclass
class Machine(Building):
    """
    Represents the physical machine constraints (Grid size, slots, etc.) of AIC machines.
    """
    time_seconds: float = 0.0 # Time for a machine to process 1 item i.e. 1 item per 2 seconds is 2.0 which 30 items/minute
    physical_input_slots: int = 0
    physical_output_slots: int = 0
    liquid_input_slots: int = 0
    liquid_output_slots: int = 0
    power_usage: float = 0.0


### ADD AIC TECH TREE
### ADD POWER RADIUS TO PYLONS AND RELAYS (RELAYS CONDITIONAL ON TECH TREE)


### Valley IV Machines ###
transport_belt = Machine(
    name="Transport Belt",
    size=(1, 1),
    description="Basic belt for transporting items.",
    time_seconds=2.0,  # 30/min
    physical_input_slots=1,
    physical_output_slots=1,
)

belt_bridge = Machine(
    name="Belt Bridge",
    size=(1, 1),
    description="",
    physical_input_slots=2,
    physical_output_slots=2,
)

splitter = Machine(
    name="Splitter",
    size=(1, 1),
    description="",
    physical_input_slots=1,
    physical_output_slots=3,
)

converger = Machine(
    name="Converger",
    size=(1, 1),
    description="",
    physical_input_slots=3,
    physical_output_slots=1,
)

item_control_port = Machine(
    name="Item Control Port",
    size=(1, 1),
    description="",
    physical_input_slots=1,
    physical_output_slots=1,
)

protocol_stash = Machine(
    name="Protocol Stash",
    size=(2, 2),
    description="",
    physical_input_slots=3,
    physical_output_slots=3,
    power_usage=5.0,
)

depot_loader = Machine(
    name="Depot Loader",
    size=(1, 3),
    description="",
    time_seconds=0.0,
    physical_input_slots=1,
    physical_output_slots=0,
    power_usage=0.0,
)

depot_unloader = Machine(
    name="Depot Unloader",
    size=(1, 3),
    description="",
    physical_input_slots=0,
    physical_output_slots=1,
)

refining_unit = Machine(
    name="Refining Unit",
    size=(3, 3),
    description="",
    time_seconds=2.0,  # 30/min
    physical_input_slots=3,
    physical_output_slots=3,
    power_usage=5.0,
)

shredding_unit = Machine(
    name="Shredding Unit",
    size=(3, 3),
    description="",
    time_seconds=2.0,  # 30/min
    physical_input_slots=3,
    physical_output_slots=3,
    power_usage=5.0,
)

fitting_unit = Machine(
    name="Fitting Unit",
    size=(3, 3),
    description="",
    time_seconds=2.0,  # 30/min
    physical_input_slots=3,
    physical_output_slots=3,
    power_usage=20.0,
)

moulding_unit = Machine(
    name="Moulding Unit",
    size=(3, 3),
    description="",
    time_seconds=2.0,  # 30/min
    physical_input_slots=3,
    physical_output_slots=3,
    power_usage=10.0,
)

seed_picking_unit = Machine(
    name="Seed-Picking Unit",
    size=(5, 5),
    description="",
    time_seconds=2.0,  # 30/min
    physical_input_slots=5,
    physical_output_slots=5,
    power_usage=10.0,
)

planting_unit = Machine(
    name="Planting Unit",
    size=(5, 5),
    description="",
    time_seconds=2.0,  # 30/min
    physical_input_slots=5,
    physical_output_slots=5,
    power_usage=20.0,
)

gearing_unit = Machine(
    name="Gearing Unit",
    size=(4, 6),
    description="",
    time_seconds=10.0,  # 6/min
    physical_input_slots=6,
    physical_output_slots=6,
    power_usage=10.0,
)

filling_unit = Machine(
    name="Filling Unit",
    size=(4, 6),
    description="",
    time_seconds=10.0,  # 6/min
    physical_input_slots=6,
    physical_output_slots=6,
    power_usage=20.0,
)

packaging_unit = Machine(
    name="Packaging Unit",
    size=(4, 6),
    description="",
    time_seconds=10.0,  # 6/min
    physical_input_slots=6,
    physical_output_slots=6,
    power_usage=20.0,
)

grinding_unit = Machine(
    name="Grinding Unit",
    size=(4, 6),
    description="",
    time_seconds=2.0,  # 30/min
    physical_input_slots=6,
    physical_output_slots=6,
    power_usage=50.0,
)

thermal_bank = Machine(
    name="Thermal Bank",
    size=(2, 2),
    description="",
    physical_input_slots=2,
)

electric_pylon = Machine(
    name="Electric Pylon",
    size=(2, 2),
    description="",
)

relay_tower = Machine(
    name="Relay Tower",
    size=(3, 3),
    description="",
)


### Wuling ###
pipe = Machine(
    name="Pipe",
    size=(1, 1),
    description="",
    on_ground=False,
    liquid_input_slots=1,
    liquid_output_slots=1,
)

pipe_bridge = Machine(
    name="Pipe Bridge",
    size=(1, 1),
    description="",
    on_ground=False,
    liquid_input_slots=2,
    liquid_output_slots=2,
)

pipe_splitter = Machine(
    name="Pipe Splitter",
    size=(1, 1),
    description="",
    on_ground=False,
    liquid_input_slots=1,
    liquid_output_slots=3,
)

pipe_converger = Machine(
    name="Pipe Converger",
    size=(1, 1),
    description="",
    on_ground=False,
    liquid_input_slots=3,
    liquid_output_slots=1,
)

pipe_control_port = Machine(
    name="Pipe Control Port",
    size=(1, 1),
    description="",
    on_ground=False,
    liquid_input_slots=1,
    liquid_output_slots=1,
)

planting_unit_wuling = Machine(
    name="Planting Unit (Wuling)",
    size=(5, 5),
    description="",
    time_seconds=2.0,  # 30/min (same as base planting)
    physical_input_slots=5,
    physical_output_slots=5,
    liquid_input_slots=1,
    power_usage=20.0,
)

filling_unit_wuling = Machine(
    name="Filling Unit (Wuling)",
    size=(4, 6),
    description="",
    time_seconds=10.0,  # 6/min (same as base filling)
    physical_input_slots=6,
    physical_output_slots=6,
    liquid_input_slots=1,
    power_usage=20.0,
)

separating_unit = Machine(
    name="Separating Unit",
    size=(4, 6),
    description="",
    time_seconds=2.0,  # 30/min
    physical_input_slots=6,
    physical_output_slots=6,
    liquid_output_slots=1,
    power_usage=50.0,
)

reactor_crucible = Machine(
    name="Reactor Crucible",
    size=(5, 5),
    description="",
    time_seconds=2.0,  # 30/min
    physical_input_slots=2,
    physical_output_slots=2,
    liquid_input_slots=2,
    liquid_output_slots=2,
    power_usage=50.0,
)

forge_of_the_sky = Machine(
    name="Forge of the Sky",
    size=(5, 5),
    description="",
    time_seconds=2.0,  # 30/min
    physical_input_slots=5,
    physical_output_slots=5,
    liquid_input_slots=1,
    power_usage=50.0,
)

fluid_pump = Machine(
    name="Fluid Pump",
    size=(3, 3),
    description="",
    time_seconds=1.0,  # 60/min
    liquid_output_slots=1,
    power_usage=10.0,
)

xiranite_pylon = Machine(
    name="Xiranite Pylon",
    size=(2, 2),
    description="",
)

xiranite_relay = Machine(
    name="Xiranite Relay",
    size=(3, 3),
    description="",
)
