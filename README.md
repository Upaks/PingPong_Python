# PingPong Python 🏓

A minimalist recreation of the Pong arcade classic using only Python’s built-in `turtle` graphics. Two paddles, one ball, and a scoreboard—perfect for practicing event handling and animation fundamentals.

## Features
- **Pure Python**: relies exclusively on the standard library (no external deps).
- **Two-Player Controls**: left paddle uses `W/S`, right paddle uses `Up/Down`.
- **Score Tracking**: `scoreboard.py` keeps both players’ points visible.
- **Modular Design**: separate classes for paddles, ball physics, and scoring.

## File Overview
- `main.py` – sets up the screen, binds controls, and runs the main game loop.
- `paddle.py` – defines paddle movement and boundary clamps.
- `ball.py` – handles ball velocity, bouncing, and reset logic after scoring.
- `scoreboard.py` – displays scores and updates them when a player scores.
- `.idea/inspectionProfiles` – IDE settings (optional for development).

## Requirements
- Python 3.x with the standard `turtle` module (pre-installed with Python).

## Getting Started
```bash
git clone https://github.com/<your-user>/PingPong_Python.git
cd PingPong_Python
python main.py
```

## Controls
- **Left Paddle**: `W` (up), `S` (down)
- **Right Paddle**: `↑` (up), `↓` (down)

## Customize & Extend
- Adjust ball speed or acceleration inside `ball.py`.
- Modify paddle size or movement speed in `paddle.py`.
- Add sound effects or power-ups by extending the main loop.

## Contributing
Pull requests are welcome—feel free to propose AI opponents, score limits, or visual enhancements. Open an issue first if you’d like to discuss a major change.
