# hardware.py

import sys
import board
import busio
import neopixel
from adafruit_mpr121 import MPR121
from config import NUM_PIXELS, PIXEL_PIN, TOUCH_THRESHOLD, RELEASE_THRESHOLD

def exit_with_error(msg):
    print(f"[ERROR] {msg}")
    sys.exit(1)

# Initialize I2C
try:
    i2c = busio.I2C(board.SCL, board.SDA)
except Exception as e:
    exit_with_error(f"Failed to initialize I2C: {e}")

# Initialize MPR121 touch sensor
try:
    mpr = MPR121(i2c)
except Exception as e:
    exit_with_error(f"Failed to initialize MPR121 sensor: {e}")

# Initialize NeoPixel strip
try:
    pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=1.0, auto_write=False)
except Exception as e:
    exit_with_error(f"Failed to initialize NeoPixels: {e}")

# Set thresholds safely
for i in range(NUM_PIXELS):
    try:
        mpr[i].threshold = TOUCH_THRESHOLD
        mpr[i].release_threshold = RELEASE_THRESHOLD
    except Exception as e:
        print(f"[WARNING] Failed to set threshold for channel {i}: {e}")
