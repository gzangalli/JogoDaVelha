import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text=" ",
                    font=("Arial", 30),
                    width=4,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo(
                    "Fim de jogo", f"O jogador {self.current_player} venceu!")
                self.window.quit()
            elif self.is_board_full():
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.window.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def run(self):
        self.window.mainloop()


game = TicTacToe()
game.run()
