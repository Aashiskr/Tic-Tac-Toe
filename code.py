def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    players = [player1_name, player2_name]
    current_player_idx = 0

    while True:
        print_board(board)
        current_player = players[current_player_idx]
        row = int(input(f"{current_player}, enter row (1-3): ")) - 1
        col = int(input(f"{current_player}, enter column (1-3): ")) - 1

        if board[row][col] != " ":
            print("That cell is already taken!")
            continue

        board[row][col] = "X" if current_player_idx == 0 else "O"

        if check_winner(board):
            print_board(board)
            print(f"{current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player_idx = (current_player_idx + 1) % 2

    print_board(board)  # Print final board after the game ends

tic_tac_toe()

