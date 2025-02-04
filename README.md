# GameSpace

## Description
GameSpace is a 2D arcade-style game built using Python and Pygame. Players control a hero character navigating through obstacles, avoiding enemies, and collecting extra lives to reach the level goal.

## Features
- Player movement in four directions
- Enemy movement with randomized directions
- Shooting mechanics for eliminating enemies
- Collision detection with barriers and enemies
- Extra life pickup system
- Background music and sound effects
- Level completion and game-over screens

## Installation
### Requirements
Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Install Dependencies
Before running the game, install the required dependencies:
```sh
pip install pygame
```

## Running the Game
To start the game, navigate to the directory where `main.py` is located and run:
```sh
python main.py
```

## Controls
- **Arrow Keys**: Move the player character
- **Spacebar**: Shoot bullets
- **ESC**: Quit the game

## File Structure
```
GameSpace/
│── main.py                # Main game script
│── sounds/                # Sound effects and music
│   │── music.wav          # Background music
│   │── button.mp3         # Shooting sound
│── images/                # Image assets
│   │── backgrounds/       # Background images
│   │── rightwalking/      # Right movement sprites
│   │── leftwalking/       # Left movement sprites
│   │── enemies/          # Enemy sprites
│   │── barriers/         # Obstacle sprites
│   │── bullet.png        # Bullet image
│── README.md              # This file
```

## Game Mechanics
- The player moves using the arrow keys and can shoot using the spacebar.
- Enemies move in random directions.
- Bullets collide with enemies and barriers.
- The player must reach the end-of-level trophy to win.
- If the player loses all lives, the game ends with a loss screen.

## Future Improvements
- Adding multiple levels with increasing difficulty.
- Enhancing AI for enemy movement.
- Adding more power-ups and weapons.

## License
This game is open-source and free to use for learning and personal projects.

## Credits
Developed using Python and Pygame.

