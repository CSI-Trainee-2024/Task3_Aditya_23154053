# Space Invaders Game
# --Aditya Singh(23154053)--
This is a simple **Space Invaders** game built using **Python** and **Pygame**. The game involves controlling a spaceship to shoot down enemies while avoiding them. The player gains points by hitting enemies with bullets, and the game ends when an enemy reaches the player.

## Table of Contents
- [Game Features](#game-features)
- [How to Run the Game](#how-to-run-the-game)
- [Requirements](#requirements)
- [Game Instructions](#game-instructions)
- [Files in the Project](#files-in-the-project)
- [How It Works](#how-it-works)
- [Key Functions](#key-functions)

## Game Features
- Control a spaceship with left and right arrow keys.
- Fire bullets using the space bar.
- Multiple enemies that move toward the player.
- Score increases for each enemy destroyed.
- The game ends when an enemy reaches the player’s position.
- Background music and sound effects (bullet firing, explosions).

## How to Run the Game
1. Clone or download this repository to your local machine.
2. Ensure you have Python installed. If not, download it from [here](https://www.python.org/downloads/).
3. Install **Pygame** by running:
   ```bash
   pip install pygame
4. Run the Python script:
    ```bash
   python main.py

## Requirements
1. Python 3.x: The game is developed using Python 3.
2. Pygame Library: This library is essential for handling the game’s graphics, input, and sound. You can install it by running pip install pygame.

## Game Instructions
1. Move your spaceship using the left and right arrow keys.
2. Press the space bar to shoot bullets at the enemies.
3. Each time you hit an enemy, you earn a point.
4. If an enemy reaches your position (at the bottom of the screen), the game will end.
5. Try to score as many points as possible before the game ends!
 
## Files in the Project
1. space_invaders.py: The main Python file containing the game logic.
2. background.png: The background image for the game.
3. player.png: The image for the player's spaceship.
4. enemy.png: The image for the enemies.
5. bullet.png: The image for the bullet.
6. background.wav: Background music played during the game.
7. laser.wav: Sound effect for firing the bullet.
8. explosion.wav: Sound effect for enemy explosion.

## How it works
The game uses Pygame for handling graphics, sound, and user input. The main components of the game include:

1. Player: Controlled by the arrow keys. The player can shoot bullets using the space bar.
2. Enemies: The enemies move horizontally and descend towards the player when they reach the screen's edge.
3. Bullets: The player fires bullets to destroy enemies. Collision detection is handled using the math module to calculate the distance between the bullet and enemies.
4. Game Over: The game ends when an enemy reaches the player's level.

## Key Functions:
Key Functions:
1. player(x, y): Renders the player's spaceship on the screen.
2. enemy(x, y, i): Renders the enemies.
3. fire_bullet(x, y): Fires a bullet from the player’s position.
4. isCollision(enemyX, enemyY, bulletX, bulletY): Checks if a bullet hits an enemy.
5. show_score(x, y): Displays the current score on the screen.
6. game_over_text(): Displays the "Game Over" message.