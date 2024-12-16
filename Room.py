class Room:
    """
    Represents a single room in the dungeon.

    Attributes:
        name (str): The name of the room (e.g., "Entrance", "Treasure Room").
        description (str): The description of the room.
        items (list): Items present in the room.
    """
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items or []  # Default to an empty list if no items
