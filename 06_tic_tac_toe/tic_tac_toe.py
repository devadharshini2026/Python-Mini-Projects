def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("=== Tic-Tac-Toe Game ===")
    print("Player 1 → X | Player 2 → O")
    print_board(board)

    while True:
        current_player = players[turn % 2]
        print(f"Player {turn % 2 + 1}'s turn ({current_player})")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
        except ValueError:
            print("Invalid input! Please enter numbers 0–2.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position! Choose between 0–2.")
            continue
        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {turn % 2 + 1} ({current_player}) wins!")
            break
        if is_full(board):
            print("🤝 It's a draw!")
            break

        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
