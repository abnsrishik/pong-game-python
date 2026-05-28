# Pong Game

Two-player Pong built in Python using OOP architecture.
Ball accelerates on every paddle hit — gets harder as the rally ,continues.

## Controls

| Player | Up | Down |
|---|---|---|
| Left (P1) | `W` | `S` |
| Right (P2) | `↑` | `↓` |

## Features

- Two-player local multiplayer
- Ball speeds up 10% on every paddle bounce (`move_speed *= 0.9`)
- Resets to center with direction flip on missed ball
- Live score display for both players

## How to Run

```bash
git clone https://github.com/abnsrishik/pong-game-python
cd pong-game-python
python main.py
```

No external dependencies. Uses Python's built-in `turtle` module.

## Architecture

| File | Class | Responsibility |
|---|---|---|
| `paddle.py` | `Paddle` | Position, up/down movement |
| `ball.py` | `Ball` | Movement, wall/paddle bounce, speed scaling, reset |
| `scoreboard.py` | `ScoreBoard` | Score tracking, display for both players |
| `main.py` | — | Game loop, collision detection, key bindings |

## What I Learned

- Passing arguments to `__init__` for reusable classes (both paddles, one class)
- Ball acceleration using speed multiplier
- Collision detection with distance + position threshold
- Two-player input binding on one screen
