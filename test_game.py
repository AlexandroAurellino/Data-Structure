from DungeonTree import DungeonTree
from Room import Room
from CombatBinaryTree import CombatBinaryTree
from Player import Player



# Create rooms
entrance = Room("Entrance", "A dark and cold room.")
hallway = Room("Hallway", "A narrow hallway.")
treasure = Room("Treasure Room", "A glittering room filled with gold.")

# Build the tree
dungeon_tree = DungeonTree(entrance)
dungeon_tree.add_room(entrance, hallway)
dungeon_tree.add_room(hallway, treasure)

# Print the dungeon map
dungeon_tree.print_map()

combat_tree = CombatBinaryTree()
combat_tree.build_tree()
combat_tree.traverse(combat_tree.root)

player = Player()
player.add_item("Potion", {"healing": 20})
player.add_item("Sword", {"damage": 50})
player.use_item("Potion")  # Heals the player
print(player.inventory)  # Check remaining inventory
