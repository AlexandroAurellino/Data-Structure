### **Assignment: Build a Text-Based Adventure Game Using Linked Lists**

#### **Objective**
Create a text-based adventure game where the player moves through different rooms in a dungeon. The dungeon's rooms will be implemented using a **Linked List**.

---

#### **Game Description**
- The player starts in the first room of the dungeon and can move **forward** or **backward** through the rooms.
- Each room will have a description and may contain challenges (like puzzles or traps) or rewards (like treasures).
- The player wins by reaching the last room and loses if their health reaches zero.

---

#### **Requirements**
1. **Classes and OOP Concepts**:
   - **Room**: Represents a single room in the dungeon.  
     Attributes:
     - `name` (e.g., "Entrance", "Treasure Room")
     - `description`
     - `next_room` (reference to the next room in the Linked List)
     - `previous_room` (reference to the previous room in the Linked List)

   - **Dungeon**: Manages the Linked List of rooms.
     Methods:
     - `add_room`: Adds a new room to the dungeon.
     - `remove_room`: Removes a room by name.
     - `navigate_forward`: Moves the player to the next room.
     - `navigate_backward`: Moves the player to the previous room.

   - **Player**: Tracks player stats.  
     Attributes:
     - `health`
     - `inventory`

2. **Gameplay**:
   - The game should start with at least 5 rooms connected in a Linked List.
   - The player can navigate between rooms using commands like `go forward` or `go backward`.
   - Display the current room’s description and allow the player to interact with it.
   - Include a small event system:
     - Traps that reduce health.
     - Treasures that can be collected into the inventory.

---

#### **Tools**
- **IDE**: Use VSCode.
- **Debugger**: Use VSCode's built-in debugger to test your code step-by-step.
- **Libraries**:
  - Python's `dataclasses` for simplified class definitions.
  - Use `os` or `time` for creating delays or clearing the console for better user experience (optional).

---

#### **Deliverables**
1. A Python file (`dungeon_game.py`) containing the game code.
2. The game should be playable from the terminal/console.

---

### **Hints**
- Use a **singly linked list** structure to connect rooms first, and then extend it to a **doubly linked list** if time permits.
- Focus on writing clean, modular code. Use methods to handle specific tasks like printing room details or handling player inputs.
- Test your Linked List implementation separately before integrating it into the game logic.

---

Once you're done, share your code here, and I'll review it for you, providing feedback on both the implementation and your understanding of the concepts. Good luck!