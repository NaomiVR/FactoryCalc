from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    """
    Represents a single item or fluid (e.g., 'Originium Ore', 'Water').
    Attributes:
        name (str): The name of the item
        icon_path (str): The file path to the item's icon image
        is_fluid (bool): Whether the item is a fluid (True) or solid (False)
        stock_bill_valley (int): The quantity of this item required in the stock bill for Valley of Heroes (if applicable)
        stock_bill_wuling (int): The quantity of this item required in the stock bill for Wuling (if applicable)
    """
    name: str
    icon_path: str
    is_fluid: bool = False
    stock_bill_valley: int = 0
    stock_bill_wuling: int = 0

    @property
    def stock_bill_per_item(self) -> int:
        # Backwards-compatible access: prefer Valley value if present, otherwise Wuling
        return self.stock_bill_valley or self.stock_bill_wuling


### Natural Resources ###
aketine = Item("Aketine", "ItemIcons/Natural_Resources_Icons/Aketine.png")
aketine_seed = Item("Aketine Seed", "ItemIcons/Natural_Resources_Icons/Aketine_Seed.png")
amber_rice = Item("Amber Rice", "ItemIcons/Natural_Resources_Icons/Amber_Rice.png")
amber_rice_seed = Item("Amber Rice Seed", "ItemIcons/Natural_Resources_Icons/Amber_Rice_Seed.png")
amethyst_ore = Item("Amethyst Ore", "ItemIcons/Natural_Resources_Icons/Amethyst_Ore.png")
buckflower = Item("Buckflower", "ItemIcons/Natural_Resources_Icons/Buckflower.png")
buckflower_seed = Item("Buckflower Seed", "ItemIcons/Natural_Resources_Icons/Buckflower_Seed.png")
citrome = Item("Citrome", "ItemIcons/Natural_Resources_Icons/Citrome.png")
citrome_seed = Item("Citrome Seed", "ItemIcons/Natural_Resources_Icons/Citrome_Seed.png")
clean_water = Item("Clean Water", "ItemIcons/Natural_Resources_Icons/Clean_Water.png", is_fluid=True)
ferrium_ore = Item("Ferrium Ore", "ItemIcons/Natural_Resources_Icons/Ferrium_Ore.png")
jincao = Item("Jincao", "ItemIcons/Natural_Resources_Icons/Jincao.png")
jincao_seed = Item("Jincao Seed", "ItemIcons/Natural_Resources_Icons/Jincao_Seed.png")
originium_ore = Item("Originium Ore", "ItemIcons/Natural_Resources_Icons/Originium_Ore.png")
redjade_ginseng = Item("Redjade Ginseng", "ItemIcons/Natural_Resources_Icons/Redjade_Ginseng.png")
redjade_ginseng_seed = Item("Redjade Ginseng Seed", "ItemIcons/Natural_Resources_Icons/Redjade_Ginseng_Seed.png")
reed_rye = Item("Reed Rye", "ItemIcons/Natural_Resources_Icons/Reed_Rye.png")
reed_rye_seed = Item("Reed Rye Seed", "ItemIcons/Natural_Resources_Icons/Reed_Rye_Seed.png")
sandleaf = Item("Sandleaf", "ItemIcons/Natural_Resources_Icons/Sandleaf.png")
sandleaf_seed = Item("Sandleaf Seed", "ItemIcons/Natural_Resources_Icons/Sandleaf_Seed.png")
tartpepper = Item("Tartpepper", "ItemIcons/Natural_Resources_Icons/Tartpepper.png")
tartpepper_seed = Item("Tartpepper Seed", "ItemIcons/Natural_Resources_Icons/Tartpepper_Seed.png")
wood = Item("Wood", "ItemIcons/Natural_Resources_Icons/Wood.png")
yazhen = Item("Yazhen", "ItemIcons/Natural_Resources_Icons/Yazhen.png")
yazhen_seed = Item("Yazhen Seed", "ItemIcons/Natural_Resources_Icons/Yazhen_Seed.png")


### AIC Products ###
aketine_powder = Item("Aketine Powder", "ItemIcons/AIC_Products_Icons/Aketine_Powder.png")
amethyst_bottle = Item("Amethyst Bottle", "ItemIcons/AIC_Products_Icons/Amethyst_Bottle.png", stock_bill_valley=2)
amethyst_bottle_clean_water = Item("Amethyst Bottle (Clean Water)", "ItemIcons/AIC_Products_Icons/Amethyst_Bottle_Clean_Water.png")
amethyst_bottle_jincao = Item("Amethyst Bottle (Jincao)", "ItemIcons/AIC_Products_Icons/Amethyst_Bottle_Jincao.png")
amethyst_bottle_yazhen = Item("Amethyst Bottle (Yazhen)", "ItemIcons/AIC_Products_Icons/Amethyst_Bottle_Yazhen.png")
amethyst_bottle_liquid_xiranite = Item("Amethyst Bottle (Liquid Xiranite)", "ItemIcons/AIC_Products_Icons/Amethyst_Bottle_Liquid_Xiranite.png")
amethyst_component = Item("Amethyst Component", "ItemIcons/AIC_Products_Icons/Amethyst_Component.png")
amethyst_fiber = Item("Amethyst Fiber", "ItemIcons/AIC_Products_Icons/Amethyst_Fiber.png")
amethyst_part = Item("Amethyst Part", "ItemIcons/AIC_Products_Icons/Amethyst_Part.png", stock_bill_valley=1)
amethyst_powder = Item("Amethyst Powder", "ItemIcons/AIC_Products_Icons/Amethyst_Powder.png")
carbon = Item("Carbon", "ItemIcons/AIC_Products_Icons/Carbon.png")
carbon_powder = Item("Carbon Powder", "ItemIcons/AIC_Products_Icons/Carbon_Powder.png")
cryston_bottle = Item("Cryston Bottle", "ItemIcons/AIC_Products_Icons/Cryston_Bottle.png")
cryston_bottle_clean_water = Item("Cryston Bottle (Clean Water)", "ItemIcons/AIC_Products_Icons/Cryston_Bottle_Clean_Water.png")
cryston_bottle_jincao = Item("Cryston Bottle (Jincao)", "ItemIcons/AIC_Products_Icons/Cryston_Bottle_Jincao.png")
cryston_bottle_yazhen = Item("Cryston Bottle (Yazhen)", "ItemIcons/AIC_Products_Icons/Cryston_Bottle_Yazhen.png")
cryston_bottle_liquid_xiranite = Item("Cryston Bottle (Liquid Xiranite)", "ItemIcons/AIC_Products_Icons/Cryston_Bottle_Liquid_Xiranite.png")
cryston_component = Item("Cryston Component", "ItemIcons/AIC_Products_Icons/Cryston_Component.png")
cryston_fiber = Item("Cryston Fiber", "ItemIcons/AIC_Products_Icons/Cryston_Fiber.png")
cryston_part = Item("Cryston Part", "ItemIcons/AIC_Products_Icons/Cryston_Part.png")
cryston_powder = Item("Cryston Powder", "ItemIcons/AIC_Products_Icons/Cryston_Powder.png")
dense_carbon_powder = Item("Dense Carbon Powder", "ItemIcons/AIC_Products_Icons/Dense_Carbon_Powder.png")
dense_ferrium_powder = Item("Dense Ferrium Powder", "ItemIcons/AIC_Products_Icons/Dense_Ferrium_Powder.png")
dense_originium_powder = Item("Dense Originium Powder", "ItemIcons/AIC_Products_Icons/Dense_Originium_Powder.png")
dense_origocrust_powder = Item("Dense Origocrust Powder", "ItemIcons/AIC_Products_Icons/Dense_Origocrust_Powder.png")
ferrium = Item("Ferrium", "ItemIcons/AIC_Products_Icons/Ferrium.png")
ferrium_bottle = Item("Ferrium Bottle", "ItemIcons/AIC_Products_Icons/Ferrium_Bottle.png")
ferrium_bottle_clean_water = Item("Ferrium Bottle (Clean Water)", "ItemIcons/AIC_Products_Icons/Ferrium_Bottle_Clean_Water.png")
ferrium_bottle_jincao = Item("Ferrium Bottle (Jincao)", "ItemIcons/AIC_Products_Icons/Ferrium_Bottle_Jincao.png")
ferrium_bottle_yazhen = Item("Ferrium Bottle (Yazhen)", "ItemIcons/AIC_Products_Icons/Ferrium_Bottle_Yazhen.png")
ferrium_bottle_liquid_xiranite = Item("Ferrium Bottle (Liquid Xiranite)", "ItemIcons/AIC_Products_Icons/Ferrium_Bottle_Liquid_Xiranite.png")
ferrium_component = Item("Ferrium Component", "ItemIcons/AIC_Products_Icons/Ferrium_Component.png")
ferrium_part = Item("Ferrium Part", "ItemIcons/AIC_Products_Icons/Ferrium_Part.png", stock_bill_valley=1)
ferrium_powder = Item("Ferrium Powder", "ItemIcons/AIC_Products_Icons/Ferrium_Powder.png")
ground_buckflower_powder = Item("Ground Buckflower Powder", "ItemIcons/AIC_Products_Icons/Ground_Buckflower_Powder.png")
ground_citrome_powder = Item("Ground Citrome Powder", "ItemIcons/AIC_Products_Icons/Ground_Citrome_Powder.png")
hc_valley_battery = Item("HC Valley Battery", "ItemIcons/AIC_Products_Icons/HC_Valley_Battery.png", stock_bill_valley=70)
jincao_solution = Item("Jincao Solution", "ItemIcons/AIC_Products_Icons/Jincao_Solution.png", is_fluid=True)
lc_valley_battery = Item("LC Valley Battery", "ItemIcons/AIC_Products_Icons/LC_Valley_Battery.png", stock_bill_valley=16)
lc_wuling_battery = Item("LC Wuling Battery", "ItemIcons/AIC_Products_Icons/LC_Wuling_Battery.png", stock_bill_wuling=25)
liquid_xiranite = Item("Liquid Xiranite", "ItemIcons/AIC_Products_Icons/Liquid_Xiranite.png", is_fluid=True)
originium_powder = Item("Originium Powder", "ItemIcons/AIC_Products_Icons/Originium_Powder.png")
origocrust = Item("Origocrust", "ItemIcons/AIC_Products_Icons/Origocrust.png", stock_bill_valley=1)
origocrust_powder = Item("Origocrust Powder", "ItemIcons/AIC_Products_Icons/Origocrust_Powder.png")
packed_origocrust = Item("Packed Origocrust", "ItemIcons/AIC_Products_Icons/Packed_Origocrust.png")
sandleaf_powder = Item("Sandleaf Powder", "ItemIcons/AIC_Products_Icons/Sandleaf_Powder.png")
sc_valley_battery = Item("SC Valley Battery", "ItemIcons/AIC_Products_Icons/SC_Valley_Battery.png", stock_bill_valley=30)
stabilized_carbon = Item("Stabilized Carbon", "ItemIcons/AIC_Products_Icons/Stabilized_Carbon.png")
steel = Item("Steel", "ItemIcons/AIC_Products_Icons/Steel.png")
steel_bottle = Item("Steel Bottle", "ItemIcons/AIC_Products_Icons/Steel_Bottle.png")
steel_bottle_clean_water = Item("Steel Bottle (Clean Water)", "ItemIcons/AIC_Products_Icons/Steel_Bottle_Clean_Water.png")
steel_bottle_jincao = Item("Steel Bottle (Jincao)", "ItemIcons/AIC_Products_Icons/Steel_Bottle_Jincao.png")
steel_bottle_yazhen = Item("Steel Bottle (Yazhen)", "ItemIcons/AIC_Products_Icons/Steel_Bottle_Yazhen.png")
steel_bottle_liquid_xiranite = Item("Steel Bottle (Liquid Xiranite)", "ItemIcons/AIC_Products_Icons/Steel_Bottle_Liquid_Xiranite.png")
steel_part = Item("Steel Part", "ItemIcons/AIC_Products_Icons/Steel_Part.png", stock_bill_valley=3)
xiranite = Item("Xiranite", "ItemIcons/AIC_Products_Icons/Xiranite.png", stock_bill_wuling=1)
xiranite_component = Item("Xiranite Component", "ItemIcons/AIC_Products_Icons/Xiranite_Component.png")
yazhen_solution = Item("Yazhen Solution", "ItemIcons/AIC_Products_Icons/Yazhen_Solution.png", is_fluid=True)


### Usable Items ###
buck_capsule_a = Item("Buck Capsule [A]", "ItemIcons/Usable_Items_Icons/Buck_Capsule_[A].png", stock_bill_valley=70)
buck_capsule_b = Item("Buck Capsule [B]", "ItemIcons/Usable_Items_Icons/Buck_Capsule_[B].png", stock_bill_valley=27)
buck_capsule_c = Item("Buck Capsule [C]", "ItemIcons/Usable_Items_Icons/Buck_Capsule_[C].png", stock_bill_valley=10)
buckflower_powder = Item("Buckflower Powder", "ItemIcons/Usable_Items_Icons/Buckflower_Powder.png")
citrome_capsule_a = Item("Citrome Capsule [A]", "ItemIcons/Usable_Items_Icons/Canned_Citrome_[A].png", stock_bill_valley=70)
citrome_capsule_b = Item("Citrome Capsule [B]", "ItemIcons/Usable_Items_Icons/Canned_Citrome_[B].png", stock_bill_valley=27)
citrome_capsule_c = Item("Citrome Capsule [C]", "ItemIcons/Usable_Items_Icons/Canned_Citrome_[C].png", stock_bill_valley=10)
citrome_powder = Item("Citrome Powder", "ItemIcons/Usable_Items_Icons/Citrome_Powder.png")
industrial_explosive = Item("Industrial Explosive", "ItemIcons/Usable_Items_Icons/Industrial_Explosive.png")
jincao_drink = Item("Jincao Drink", "ItemIcons/Usable_Items_Icons/Jincao_Drink.png", stock_bill_wuling=16)
jincao_powder = Item("Jincao Powder", "ItemIcons/Usable_Items_Icons/Jincao_Powder.png")
yazhen_powder = Item("Yazhen Powder", "ItemIcons/Usable_Items_Icons/Yazhen_Powder.png")
yazhen_syringe_c = Item("Yazhen Syringe [C]", "ItemIcons/Usable_Items_Icons/Yazhen_Syringe_[C].png", stock_bill_wuling=16)

ITEM_REGISTRY = {v.name: v for k, v in vars().items() if isinstance(v, Item)}