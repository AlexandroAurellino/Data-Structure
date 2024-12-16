from DungeonGraph import DungeonGraph

# Create a dungeon graph
dungeon = DungeonGraph()

# Add rooms
dungeon.add_room("Entrance")
dungeon.add_room("Hallway")
dungeon.add_room("Treasure Room")
dungeon.add_room("Boss Room")
dungeon.add_room("Secret Room")

# Connect rooms
dungeon.connect_rooms("Entrance", "Hallway")
dungeon.connect_rooms("Hallway", "Treasure Room")
dungeon.connect_rooms("Hallway", "Boss Room")
dungeon.connect_rooms("Treasure Room", "Secret Room", bidirectional=False)

# Display the dungeon map
dungeon.display_map()

# Find shortest path from Entrance to Secret Room
path = dungeon.navigate("Entrance", "Secret Room")
if path:
    print(f"Path to Secret Room: {' -> '.join(path)}")
else:
    print("No path found!")
