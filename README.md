# Asteroid Game

A simple Asteroids-style game built with Python and Pygame as part of Boot.dev. Fly around, shoot asteroids, and avoid collisions. Larger asteroids split into smaller ones when hit.

## Run

Requires Python 3.13 or newer and `uv`.

```bash
git clone https://github.com/Raghavgali/asteroid_game.git
cd asteroid_game
uv run main.py
```

`uv` installs the project dependencies automatically.

## Controls

| Key | Action |
| --- | --- |
| W / S | Move forward / backward |
| A / D | Rotate left / right |
| Space | Shoot |

Shots have a 0.3-second cooldown. Colliding with an asteroid ends the game. Close the window to quit.
