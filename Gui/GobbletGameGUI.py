import tkinter as tk

class GobbletGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gobblet Game")

        # GUI Components
        self.board_buttons = [[None] * 4 for _ in range(4)]

        # Create board buttons
        for i in range(4):
            for j in range(4):
                btn = tk.Button(master, text="", width=8, height=4)
                btn.grid(row=i, column=j)
                self.board_buttons[i][j] = btn

        # Game Status Label
        self.status_label = tk.Label(master, text="Player 1's turn", font=('Helvetica', 12))
        self.status_label.grid(row=5, columnspan=4)

        # Game Options
        self.restart_button = tk.Button(master, text="Restart Game", command=self.restart_game)
        self.restart_button.grid(row=6, columnspan=4)

    def restart_game(self):
        # Restart the game
        self.update_board()
        self.status_label.config(text="Player 1's turn")

    def update_board(self):
        # Update the board buttons based on the game state (dummy data)
        dummy_board_state = [
            ["", "", "", ""],
            ["", "X", "", ""],
            ["", "", "O", ""],
            ["", "", "", ""]
        ]

        for i in range(4):
            for j in range(4):
                text = dummy_board_state[i][j]
                self.board_buttons[i][j].config(text=text)

if __name__ == "__main__":
    root = tk.Tk()
    app = GobbletGUI(root)
    root.mainloop()
