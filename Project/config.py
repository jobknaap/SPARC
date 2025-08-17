# config.py

import board

# LED Configuration
NUM_PIXELS = 9
PIXEL_PIN = board.D18

# Colors
CALM_COLORS = [
    (0x00, 0x9a, 0xd9),  # Blue
    (0xea, 0x51, 0x83),  # Pink
    (0x91, 0x31, 0x89),  # Purple
    (0x36, 0x46, 0x97),  # Dark blue
    (0x20, 0x84, 0x4e),  # Green
    (0xe5, 0xa1, 0x00),  # Yellow
    (0xed, 0x71, 0x02),  # Orange
    (0xc5, 0x1a, 0x1b),  # Red
    (0x76, 0xb7, 0x2a),  # Lime green
    (0x00, 0x9c, 0x91),  # Teal
]

COLOR_PAIRS = [
    ((255, 0, 0), (0, 0, 255)),     # Red vs Blue
    ((255, 255, 0), (128, 0, 128)), # Yellow vs Purple
    ((0, 255, 0), (255, 0, 255)),   # Green vs Magenta
    ((255, 165, 0), (0, 255, 255)), # Orange vs Cyan
    ((255, 105, 180), (0, 128, 128))# Hot Pink vs Teal
]

LAP_COLORS = [
	(0, 255, 0),     # Green
	(0, 0, 255),     # Blue
	(255, 255, 0),   # Yellow
	(255, 0, 255),   # Magenta
	(255, 165, 0),   # Orange
]

# Touch to grid index
INPUT_TO_GRID_INDEX = {
    8: 0, 5: 1, 2: 2,
    7: 3, 4: 4, 1: 5,
    6: 6, 3: 7, 0: 8
}

GRID_TO_LED_INDEX = {
    0: 0, 1: 1, 2: 2,
    3: 5, 4: 4, 5: 3,
    6: 6, 7: 7, 8: 8
}

# Win conditions
WIN_LINES = (
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
)

# Touch sensitivity
TOUCH_THRESHOLD = 3
RELEASE_THRESHOLD = 1
