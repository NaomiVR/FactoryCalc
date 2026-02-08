from items import Item
from machines import Machine
from recipes import Recipe

class Database:
    def __init__(self, items: dict[str, Item] = None, machines: dict[str, Machine] = None, recipes: list[Recipe] = None) -> None:
        self.items: dict[str, Item] = items if items is not None else {}
        self.machines: dict[str, Machine] = machines if machines is not None else {}
        self.recipes: list[Recipe] = recipes if recipes is not None else []

        self._recipes_by_output: dict[str, list[Recipe]] = {}
        self._recipes_by_machine: dict[str, list[Recipe]] = {}

        self._rebuild_indexes()

    def _rebuild_indexes(self) -> None:
        self._recipes_by_output.clear()
        self._recipes_by_machine.clear()

        for recipe in self.recipes:
            for output_item in recipe.output.keys():
                if output_item not in self._recipes_by_output:
                    self._recipes_by_output[output_item.name] = []
                self._recipes_by_output[output_item.name].append(recipe)

            m_name = recipe.machine.name
            if m_name not in self._recipes_by_machine:
                self._recipes_by_machine[m_name] = []
            self._recipes_by_machine[m_name].append(recipe)

    def get_item(self, key: str) -> Item:
        return self.items.get(key)

    def get_machine(self, key: str) -> Machine:
        return self.machines.get(key)

    def get_recipes_for_item(self, lookup: str) -> list[Recipe]:
        item_obj = self.items.get(lookup)
        if item_obj:
            return self._recipes_by_output.get(item_obj.name, [])
        return self._recipes_by_output.get(lookup, [])

    def get_recipes_for_machine(self, lookup: str) -> list[Recipe]:
        mach_obj = self.machines.get(lookup)
        if mach_obj:
            return self._recipes_by_machine.get(mach_obj.name, [])
        return self._recipes_by_machine.get(lookup, [])
