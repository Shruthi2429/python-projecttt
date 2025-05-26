shruthi.p/1AY24AI104/o sec
def is_valid_chess_board(board):
    valid_positions = [f"{row}{col}" for row in '12345678' for col in 'abcdefgh']
    valid_pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    
    white_pieces = 0
    black_pieces = 0
    white_pawns = 0
    black_pawns = 0
    white_kings = 0
    black_kings = 0

    for position, piece in board.items():
        # Check for valid board positions
        if position not in valid_positions:
            print(f"Invalid board position: {position}")
            return False
        
        # Check for valid piece name
        if len(piece) < 2 or piece[0] not in ['w', 'b'] or piece[1:] not in valid_pieces:
            print(f"Invalid piece: {piece}")
            return False

        # Count pieces by type
        if piece[0] == 'w':
            white_pieces += 1
            if piece[1:] == 'pawn':
                white_pawns += 1
            if piece[1:] == 'king':
                white_kings += 1
        else:
            black_pieces += 1
            if piece[1:] == 'pawn':
                black_pawns += 1
            if piece[1:] == 'king':
                black_kings += 1

    # Rule checks
    if white_kings != 1 or black_kings != 1:
        print("There must be exactly one white king and one black king.")
        return False
    if white_pawns > 8 or black_pawns > 8:
        print("There can be at most 8 pawns per side.")
        return False
    if white_pieces > 16 or black_pieces > 16:
        print("There can be at most 16 pieces per side.")
        return False

    return True

# Example dictionary
chess_board = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking', '2h': 'bpawn',
    '2e': 'bpawn', '4e': 'wpawn'
}

# Run validation
if is_valid_chess_board(chess_board):
    print("This is a valid chess board.")
else:
    print("This is NOT a valid chess board.")
