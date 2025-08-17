# game_simon.py

import time
import random
from config import NUM_PIXELS, INPUT_TO_GRID_INDEX, CALM_COLORS
from hardware import mpr, pixels
from animations import CalmFadeAnimator, celebratory_anim, clear_pixels, set_grid_led, blink_grid_led


def wait_for_touch(valid_indices=None):
    while True:
        for touch_idx in range(NUM_PIXELS):
            if mpr[touch_idx].value:
                grid_index = INPUT_TO_GRID_INDEX.get(touch_idx)
                if grid_index is not None and (valid_indices is None or grid_index in valid_indices):
                    while mpr[touch_idx].value:
                        time.sleep(0.01)
                    time.sleep(0.1)
                    return grid_index
        time.sleep(0.01)


def show_score(score):
    clear_pixels()
    from config import GRID_TO_LED_INDEX, LAP_COLORS
    for point in range(score):
        led_index = GRID_TO_LED_INDEX[point % NUM_PIXELS]
        lap_num = point // NUM_PIXELS
        color = LAP_COLORS[lap_num % len(LAP_COLORS)]
        pixels[led_index] = color
        pixels.show()
        time.sleep(0.25)
    time.sleep(2)
    clear_pixels()


def run():
    animator = CalmFadeAnimator(pixels, CALM_COLORS)

    while True:
        while not any(mpr[i].value for i in range(NUM_PIXELS)):
            animator.animate()
            time.sleep(0.02)

        clear_pixels()
        time.sleep(0.5)

        sequence = []

        while True:
            sequence.append(random.randint(0, NUM_PIXELS - 1))

            for pad in sequence:
                duration = 0.4 if len(sequence) > 3 else 0.55
                blinks = 2 if len(sequence) == 1 else 1
                blink_grid_led(pad, CALM_COLORS[pad % len(CALM_COLORS)], duration, blinks)

            for expected_pad in sequence:
                touched = wait_for_touch()
                if touched != expected_pad:
                    set_grid_led(touched, (255, 0, 0))
                    for _ in range(3):
                        blink_grid_led(expected_pad, CALM_COLORS[expected_pad % len(CALM_COLORS)], 0.4)
                    show_score(len(sequence))
                    break
                blink_grid_led(touched, CALM_COLORS[touched % len(CALM_COLORS)], 0.3)
            else:
                time.sleep(0.6)
                continue

            break
