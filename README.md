# Adventure Maze Game

The Adventure Maze Game is a **text-based adventure game** where players explore a mysterious world filled with **dark rooms, magical artifacts, enemies, and hidden secrets**. Players navigate using **cardinal directions**, collect and craft items, and defeat enemies to progress.

## Features
- **Exploration**: Move through different rooms using `Go North`, `Go South`, etc.
- **Dark Rooms**: Some rooms are too dark to see without a `Lantern`.
- **Inventory System**: Collect and drop items.
- **Crafting**: Combine specific items to create powerful tools like the `Magic Staff`.
- **Enemies**: Defeat enemies like the `Dark Sorcerer` using special weapons.
- **Locked Doors**: Use keys and passcodes to unlock hidden areas.

## Installation
1. **Clone the repository:**
   ```bash
   git clone git@github.com/thechrislewis/Adventure-Game.git
   cd Adventure-Game
   ```
2. **Ensure Python 3 is installed.**
3. **Run the game:**
   ```bash
   python "MazeGame final.py"
   ```

## Files
### 0. inventory.py inventory2.py move.py move2.py
   - The Basic game. Use to teach the game logic. Not very complex. 
### 1. `MazeGame final.py`
   - The main game script that handles movement, inventory, crafting, enemies, and dark rooms.
### 2. `game_data final.json`
   - Stores all the rooms, descriptions, items, and paths.
### 3. `MazeGame step 1.py` - `MazeGame step 5.py`
   - Different development stages of the game.
### 4. `MazeGame big.py`
   - A larger version of the game with extended features.
### 5. `README.md`
   - Instructions for installation, gameplay, and contribution.

## How to Play
- **Move Around**: `Go North`, `Go East`, etc.
- **Pick Up Items**: `Get Lantern`
- **Drop Items**: `Drop Sword`
- **Use Passcodes**: `Passcode 8915` (for locked rooms)
- **Craft Items**: `Craft Magic Staff` (requires `Crystal Shard`, `Wooden Stick`, `Enchanted Core`)
- **Fight Enemies**: Some enemies require special items to defeat.

## Contributing
1. **Fork the repository.**
2. **Create a new branch:** `git checkout -b feature-name`
3. **Commit your changes:** `git commit -m "Added new feature"`
4. **Push the branch:** `git push origin feature-name`
5. **Submit a pull request!**

## License
This project is open-source and available under the MIT License.


