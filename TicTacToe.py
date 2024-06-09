import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.handle_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Add a turn indicator label
        self.turn_label = tk.Label(self.root, text=f"Turn: {self.current_player}", font=("Arial", 14))
        self.turn_label.grid(row=3, columnspan=3)

        self.root.mainloop()

    def handle_click(self, index):
        if not self.board[index]:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.root.quit()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.root.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"Turn: {self.current_player}")
    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

if __name__ == "__main__":
    TicTacToe()
