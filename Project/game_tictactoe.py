# game_tictactoe.py

import time
from config import NUM_PIXELS, COLOR_PAIRS, INPUT_TO_GRID_INDEX, WIN_LINES, CALM_COLORS
from animations import CalmFadeAnimator, celebratory_anim, clear_pixels, set_grid_led, highlight_win_line
from hardware import mpr, pixels


def check_win(board):
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def get_win_line(board):
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return (a, b, c)
    return None


def game_result(board):
    winner = check_win(board)
    if winner:
        return winner
    if None not in board:
        return "draw"
    return None


def update_display(board, players, default_color=(80, 80, 80)):
    from config import GRID_TO_LED_INDEX
    for i, val in enumerate(board):
        pixels[GRID_TO_LED_INDEX[i]] = players.get(val, default_color)
    pixels.show()


def get_touch(available_only=False, board=None):
    while True:
        for touch_idx in range(NUM_PIXELS):
            if mpr[touch_idx].value:
                grid_index = INPUT_TO_GRID_INDEX.get(touch_idx)
                if grid_index is not None:
                    if not available_only or (board and board[grid_index] is None):
                        return grid_index
        time.sleep(0.01)


def run():
    board = [None] * NUM_PIXELS
    animator = CalmFadeAnimator(pixels, CALM_COLORS)
    color_pair_index = 0
    players = {}

    while True:
        while not any(mpr[i].value for i in range(NUM_PIXELS)):
            animator.animate()
            time.sleep(0.02)

        board = [None] * NUM_PIXELS
        pair = COLOR_PAIRS[color_pair_index]
        color_pair_index = (color_pair_index + 1) % len(COLOR_PAIRS)
        players[1], players[2] = pair

        first_move = get_touch()
        board[first_move] = 1
        current_player = 2
        update_display(board, players)

        while (result := game_result(board)) is None:
            move = get_touch(available_only=True, board=board)
            board[move] = current_player
            current_player = 1 if current_player == 2 else 2
            update_display(board, players)

        if result in players:
            win_line = get_win_line(board)
            if win_line:
                highlight_win_line(win_line, players[result])
            celebratory_anim(pixels, board, players[result])
        else:
            mix = tuple((players[1][i] + players[2][i]) // 2 for i in range(3))
            celebratory_anim(pixels, board, mix)

        time.sleep(1)
