# GameSpace

## Description
GameSpace is a 2D arcade-style game built using Python and Pygame. Players control a hero character navigating through obstacles, avoiding enemies, and collecting extra lives to reach the level goal.

## Game Objective & Storyline
GameSpace was created during a **national 2-day GameDev hackathon**, where I participated solo. Although I did not win, it was a great learning experience. Due to my solo participation, there might be some minor bugs in the game.

The game is designed as a **labyrinth through space trash**, aiming to raise awareness about the real-world issue of space debris. Players must carefully navigate the space environment, avoiding obstacles and enemies, while collecting resources to survive.

## Why Pygame?
Pygame was chosen for this project because it is:
- Lightweight and beginner-friendly for 2D game development.
- Provides built-in support for graphics, sound, and event handling.
- Well-suited for simple arcade-style games without the need for heavy engines like Unity or Unreal.

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

## Code Breakdown

### 1. The Game Loop
The main loop of the game runs continuously and:
- Listens for user inputs (movement, shooting, quitting the game)
- Updates the player, enemy, and bullet positions
- Detects collisions between objects
- Draws the updated game scene onto the window

Example from `main.py`:
```python
while run:
    for e in pygame.event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN and e.key == K_SPACE:
            hero.fire()

    if not finish:
        window.blit(level1, (0, 0))
        hero.update()
        hero.animation()
        barriers.draw(window)
        enemiesdiff1.draw(window)
        enemiesdiff1.update()
        bullets.draw(window)
        bullets.update()
    pygame.display.update()
    clock.tick(fps)
```

### 2. Player Class (`Player`)
Handles movement, animations, and shooting.
```python
class Player(GameSprite):
    def __init__(self, filename, x, y, width, height, x_speed, y_speed, count, left, right):
        super().__init__(filename, x, y, width, height)
        self.life = lifes
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.x_speed = -5
            self.left = True
            self.right = False
        elif keys[K_RIGHT]:
            self.x_speed = 5
            self.left = False
            self.right = True
        else:
            self.x_speed = 0

        self.rect.x += self.x_speed
```

### 3. Enemy AI (`Enemy`)
Enemies move randomly across the screen, changing direction at intervals.
```python
class Enemy(GameSprite):
    def __init__(self, filename, x, y, width, height, speed):
        super().__init__(filename, x, y, width, height)
        self.speed = speed

    def update(self):
        direction = randint(0, 3)
        if direction == 0 and self.rect.x > 5:
            self.rect.x += self.speed
        elif direction == 1 and self.rect.x < window_width - 100:
            self.rect.x -= self.speed
```

### 4. Shooting Mechanic (`Bullet`)
The player can shoot bullets that move across the screen.
```python
class Bullet(GameSprite):
    def __init__(self, filename, x, y, width, height):
        super().__init__(filename, x, y, width, height)
        self.speed = 10
    def update(self):
        self.rect.x += self.speed
        if self.rect.x + 10 > window_width:
            self.kill()
```

![GameSpace Demo](imgs/demoSpace.gif)

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

