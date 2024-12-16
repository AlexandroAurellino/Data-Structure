from Graph import Graph

class DungeonGraph(Graph):
    """
    Extends the Graph class to represent a dungeon map.
    """
    def __init__(self):
        super().__init__()

    def add_room(self, room_name):
        """
        Adds a room to the dungeon graph.
        """
        self.add_node(room_name)

    def connect_rooms(self, room1, room2, bidirectional=True):
        """
        Connects two rooms with a path.
        """
        self.add_edge(room1, room2, bidirectional)

    def display_map(self):
        """
        Displays the dungeon map.
        """
        print("Dungeon Map:")
        self.display()
        
    def navigate(self, start, destination):
        """
        Finds the shortest path between start and destination using BFS.
        """
        from collections import deque

        if start not in self.adjacency_list or destination not in self.adjacency_list:
            return None

        visited = set()
        queue = deque([(start, [start])])  # (current_node, path)

        while queue:
            current, path = queue.popleft()

            if current == destination:
                return path

            visited.add(current)

            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return None  # No path found
