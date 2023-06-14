def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")


def check_winner(board):
    # Verifica as linhas
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Verifica as colunas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Verifica as diagonais
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = "X"
    game_over = False

    print("Bem-vindo ao Jogo da Velha!")
    print_board(board)

    while not game_over:
        print(f"É a vez do jogador {current_player}")
        row = int(input("Informe o número da linha (0-2): "))
        col = int(input("Informe o número da coluna (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)

            if check_winner(board):
                print(f"O jogador {current_player} venceu!")
                game_over = True
            elif " " not in board[0] and " " not in board[1] and " " not in board[2]:
                print("Empate!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Essa posição já está ocupada. Tente novamente.")


play_game()
