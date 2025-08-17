# main.py

import os
import sys
import threading
import keyboard
from animations import clear_pixels
import game_tictactoe
import game_simon

running = True


def key_listener():
    global running
    while True:
        if keyboard.is_pressed("esc"):
            running = False
            clear_pixels()
            os._exit(0)
        elif keyboard.is_pressed("1"):
            restart_game("tictactoe")
        elif keyboard.is_pressed("2"):
            restart_game("simon")
        threading.Event().wait(0.05)


def restart_game(game_name):
    clear_pixels()
    os.execlp("python3", "python3", __file__, game_name)


def main():
    current_game = sys.argv[1] if len(sys.argv) > 1 else "tictactoe"
    threading.Thread(target=key_listener, daemon=True).start()

    while running:
        if current_game == "tictactoe":
            game_tictactoe.run()
        elif current_game == "simon":
            game_simon.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_pixels()
