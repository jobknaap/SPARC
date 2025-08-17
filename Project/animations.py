# animations.py

import time
import random
from config import NUM_PIXELS, GRID_TO_LED_INDEX


class CalmFadeAnimator:
    """Smooth fading animation for each pixel using randomized palette cycling."""
    def __init__(self, pixels, palette, speed=0.02, step_size=4):
        self.pixels = pixels
        self.speed = speed
        self.step_size = step_size
        self.num_pixels = len(pixels)
        self.palettes = [random.sample(palette, len(palette)) for _ in range(self.num_pixels)]
        self.indices = [0] * self.num_pixels
        self.current = [p[0] for p in self.palettes]
        self.targets = [p[1 % len(p)] for p in self.palettes]

    def animate(self):
        for i in range(self.num_pixels):
            current = self.current[i]
            target = self.targets[i]
            new_color = self._interpolate(current, target)
            self.current[i] = new_color
            self.pixels[i] = new_color

            if new_color == target:
                self.indices[i] = (self.indices[i] + 1) % len(self.palettes[i])
                self.targets[i] = self.palettes[i][(self.indices[i] + 1) % len(self.palettes[i])]

        self.pixels.show()
        time.sleep(self.speed)

    def _interpolate(self, c1, c2):
        return tuple(self._step_channel(c1[i], c2[i]) for i in range(3))

    def _step_channel(self, current, target):
        if abs(current - target) <= self.step_size:
            return target
        return current + self.step_size if current < target else current - self.step_size


def celebratory_anim(pixels, board_vals, *colors):
    """Celebration effect that blinks LEDs with given colors."""
    from animations import clear_pixels

    primary = colors[0]
    secondary = colors[-1] if len(colors) > 1 else primary
    for _ in range(8):
        for i in range(NUM_PIXELS):
            pixels[GRID_TO_LED_INDEX[i]] = primary if board_vals[i] else secondary
        pixels.show()
        time.sleep(0.2)
        clear_pixels()
        time.sleep(0.2)


def fade_color(start_color, end_color, steps):
    """Generate interpolated color steps."""
    return [
        tuple(
            int(start_color[i] + (end_color[i] - start_color[i]) * step / steps)
            for i in range(3)
        )
        for step in range(steps + 1)
    ]


def snake_animation(pixels, led_mapping, colors, step_time=0.05, fade_steps=5):
    """Animated snake effect moving across LEDs with fading."""
    from animations import clear_pixels

    for led in led_mapping:
        pixels[led] = (0, 0, 0)
    pixels.show()

    prev_led = None
    for i, led in enumerate(led_mapping):
        color = colors[i % len(colors)]
        if prev_led is None:
            for c in fade_color((0, 0, 0), color, fade_steps):
                pixels[led] = c
                pixels.show()
                time.sleep(step_time)
        else:
            prev_color = pixels[prev_led]
            for step in range(fade_steps + 1):
                fade_out = tuple(int(prev_color[j] * (1 - step / fade_steps)) for j in range(3))
                fade_in = tuple(int(color[j] * step / fade_steps) for j in range(3))
                pixels[prev_led] = fade_out
                pixels[led] = fade_in
                pixels.show()
                time.sleep(step_time)
            pixels[prev_led] = (0, 0, 0)

        prev_led = led

    last_color = pixels[prev_led]
    for step in range(fade_steps + 1):
        fade_out = tuple(int(last_color[i] * (1 - step / fade_steps)) for i in range(3))
        pixels[prev_led] = fade_out
        pixels.show()
        time.sleep(step_time)
    pixels[prev_led] = (0, 0, 0)
    pixels.show()


def clear_pixels():
    """Turn off all pixels."""
    from hardware import pixels
    for i in range(NUM_PIXELS):
        pixels[i] = (0, 0, 0)
    pixels.show()


def set_grid_led(index, color):
    """Set color of a grid cell and immediately show."""
    from hardware import pixels
    from config import GRID_TO_LED_INDEX
    pixels[GRID_TO_LED_INDEX[index]] = color
    pixels.show()


def blink_grid_led(index, color, duration=0.4, times=1):
    """Blink a specific grid LED with given color and timing."""
    from time import sleep
    from config import GRID_TO_LED_INDEX
    from hardware import pixels
    for _ in range(times):
        pixels[GRID_TO_LED_INDEX[index]] = color
        pixels.show()
        sleep(duration)
        pixels[GRID_TO_LED_INDEX[index]] = (0, 0, 0)
        pixels.show()
        sleep(duration * 0.8)


def highlight_win_line(win_line, color, repeat=4, delay=0.3):
    """Highlight winning line on the grid."""
    from time import sleep
    from config import NUM_PIXELS, GRID_TO_LED_INDEX
    from hardware import pixels
    from animations import clear_pixels

    for _ in range(repeat):
        for i in range(NUM_PIXELS):
            pixels[GRID_TO_LED_INDEX[i]] = color if i in win_line else (0, 0, 0)
        pixels.show()
        sleep(delay)
        clear_pixels()
        sleep(0.2)
