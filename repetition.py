import chess

import chess

def check_threefold_repetition(moves_str):
    moves = moves_str.split()  # Split the string of moves into a list
    positions_count = {}  # Dictionary to store counts of positions encountered
    board = chess.Board()

    # Loop through each move in the provided sequence
    for move in moves:
        # Check for threefold repetition only for the last position
        if move == moves[-1]:
            last_position = board.epd()
            positions_count[last_position] = positions_count.get(last_position, 0) + 1
            if positions_count[last_position] >= 3:
                return True

        board.push_san(move)

    return False