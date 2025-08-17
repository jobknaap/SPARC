# LED Grid Game System 🎮💡

This project implements interactive games playable on a 3x3 touch grid with LED feedback. Each game features distinct animations, colors, and gameplay logic—optimized for microcontroller environments such as a Raspberry Pi with NeoPixels and an MPR121 touch sensor.

---

## Contents

- `main.py` — Central launcher to switch between games
- `hardware.py` — Initialization of touch sensor and LED strip
- `animations.py` — Visual effects and utility functions
- `config.py` — Constants like colors, mappings, and win conditions
- `game_simon.py` — Simon Says game with a color sequence
- `game_tictactoe.py` — Two-player Tic Tac Toe

---

## Games

### Simon Says

Repeat the color sequence shown on the grid. Each round adds a new color. How long can you keep up?

### Tic Tac Toe

Two players take turns marking the grid. The first to align three colors in a row, column, or diagonal wins!

---

##  Hardware Requirements

- Raspberry Pi (or compatible board)
- NeoPixel LED strip (9 LEDs)
- Adafruit MPR121 Capacitive Touch Sensor
- Connected via I2C
- Python 3.x
- Required Python packages:
  - `adafruit-circuitpython-mpr121`
  - `adafruit-circuitpython-neopixel`
  - `keyboard` (desktop only, for key input)

---

## Controls

### Via keyboard:
- `1` → Start Tic Tac Toe
- `2` → Start Simon Says
- `Esc` → Exit the program

---

## Getting Started

1. Install dependencies:
   ```bash
   pip install adafruit-circuitpython-mpr121 adafruit-circuitpython-neopixel keyboard
   ```

2. Launch the system:
   ```bash
   python3 main.py
   ```

3. Use the keyboard to switch between games.

---

## Project Structure

```text
.
├── animations.py      # Animations & helper functions (like clear_pixels)
├── config.py          # Grid mappings, colors, win conditions
├── game_simon.py      # Simon Says game
├── game_tictactoe.py  # Tic Tac Toe game
├── hardware.py        # MPR121 and NeoPixel initialization
└── main.py            # Entry point and game selector
```
