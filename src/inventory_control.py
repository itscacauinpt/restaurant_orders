class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.available_dishes = set()
        self.inventory = {ingredient: 0 for ingredient in self.MINIMUM_INVENTORY.keys()}

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] < self.MINIMUM_INVENTORY[ingredient]:
                self.inventory[ingredient] += 1
            else:
                return False

    def get_quantities_to_buy(self):
        return self.inventory

    def get_available_dishes(self):
        for dish, ingredients in self.INGREDIENTS.items():
            track = 0

            for ingredient in ingredients:
                if self.inventory[ingredient] < self.MINIMUM_INVENTORY[ingredient]:
                    track += 1

            if track == len(ingredients):
                self.available_dishes.add(dish)

        return self.available_dishes
