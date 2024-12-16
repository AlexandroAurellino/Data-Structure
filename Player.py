class Player:
    """
    Tracks player stats and inventory.

    Attributes:
        health (int): The player's current health.
        inventory (dict): A hash map representing the player's inventory.
    """

    def __init__(self):
        self.health = 1000
        self.inventory = {}  # Key: Item name, Value: Item properties (e.g., damage, healing)

    def add_item(self, item_name, properties):
        """
        Adds an item to the inventory.
        """
        self.inventory[item_name] = properties
    
    def remove_item(self, item_name):
        """
        Removes an item from the inventory.
        """
        if item_name in self.inventory:
            del self.inventory[item_name]
        else:
            print(f"Item '{item_name}' not found in inventory.")

    def use_item(self, item_name):
        """
        Uses an item from the inventory.
        """
        if item_name in self.inventory:
            item = self.inventory[item_name]
            # Example: Heal the player if it's a healing item
            if "healing" in item:
                self.health += item["healing"]
                print(f"Used {item_name}. Health is now {self.health}.")
            self.remove_item(item_name)
        else:
            print(f"Item '{item_name}' not found in inventory.")