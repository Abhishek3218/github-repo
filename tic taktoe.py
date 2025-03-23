import tkinter as tk
from tkinter import messagebox
import time

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.window.configure(bg="#1a1a2e")
        self.window.resizable(False, False)

        title = tk.Label(
            self.window,
            text="Tic Tac Toe",
            font=("Arial", 32, "bold"),
            bg="#1a1a2e",
            fg="#00fff5"
        )
        title.grid(row=0, column=0, columnspan=3, pady=20)
        self.animate_neon(title)

        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text="",
                    font=("Arial", 24, "bold"),
                    width=5,
                    height=2,
                    bg="#16213e",
                    fg="#00fff5",
                    relief="raised",
                    bd=5,
                    activebackground="#0f3460",
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i+1, column=j, padx=8, pady=8)
                self.buttons.append(button)

                button.bind("<Enter>", lambda e, btn=button: self.on_hover(btn, True))
                button.bind("<Leave>", lambda e, btn=button: self.on_hover(btn, False))

        reset_button = tk.Button(
            self.window,
            text="Reset Game",
            font=("Arial", 14, "bold"),
            bg="#e94560",
            fg="white",
            relief="raised",
            bd=3,
            command=self.reset_game
        )
        reset_button.grid(row=4, column=0, columnspan=3, pady=20)

        self.turn_label = tk.Label(
            self.window,
            text=f"Player {self.current_player}'s turn",
            font=("Arial", 16, "bold"),
            bg="#1a1a2e",
            fg="#00fff5"
        )
        self.turn_label.grid(row=5, column=0, columnspan=3, pady=10)
        self.animate_neon(self.turn_label)

    def animate_neon(self, widget):
        """Enhanced pulsing neon effect to widgets"""
        x_colors = ["#00ff88", "#00ee77", "#00dd66", "#00ee77", "#00ff88"] 
        o_colors = ["#ff3366", "#ee2255", "#dd1144", "#ee2255", "#ff3366"]  
        
        def pulse(index=0):
            if isinstance(widget, tk.Button) and widget["text"] == "X":
                widget.configure(fg=x_colors[index])
            elif isinstance(widget, tk.Button) and widget["text"] == "O":
                widget.configure(fg=o_colors[index])
            else:
                widget.configure(fg=["#00fff5", "#00e5ff", "#00d5ff", "#00e5ff", "#00fff5"][index])
            index = (index + 1) % 5
            self.window.after(200, lambda: pulse(index))
        pulse()

    def on_hover(self, button, entering):
        """Enhanced hover effect with glow"""
        if entering:
            button.configure(bg="#0f3460", relief="ridge")
            if button["text"] == "X":
                button.configure(fg="#00ff99")
            elif button["text"] == "O":
                button.configure(fg="#ff4477")
        else:
            button.configure(bg="#16213e", relief="raised")
            if button["text"] == "X":
                button.configure(fg="#00ff88")
            elif button["text"] == "O":
                button.configure(fg="#ff3366")

    def button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == "":

            self.buttons[index].configure(relief="sunken")
            self.window.after(100, lambda: self.buttons[index].configure(relief="raised"))
            
            self.board[index] = self.current_player
            
            color = "#00ff88" if self.current_player == "X" else "#ff3366"
            self.buttons[index].config(
                text=self.current_player,
                bg="#16213e",
                fg=color,
                font=("Arial", 24, "bold")
            )
            
            self.animate_neon(self.buttons[index])
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != "":
                return True

        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "":
                return True

        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
        
        return False

    def reset_game(self):

        for button in self.buttons:
            button.config(bg="#e94560")
            self.window.after(100, lambda btn=button: btn.config(bg="#ff3366"))
        self.window.after(200, self._complete_reset)

    def _complete_reset(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="", bg="#16213e", fg="#00fff5")
        self.turn_label.config(text=f"Player {self.current_player}'s turn")

    def run(self):
        self.window.mainloop()

def draw_text(board, message):
    board.penup()
    board.goto(0, 160)
    board.color("black")
    board.write(message, align="center", font=("Arial", 16, "normal"))
    board.color("black")

def is_board_full(board_state):
    return all(cell != "" for row in board_state for cell in row)

def click_handler(x, y, board, board_state, current_player):
    # Convert click coordinates to grid position
    row = int((100 - y) // 100)
    col = int((x + 150) // 100)
    
    if 0 <= row <= 2 and 0 <= col <= 2 and board_state[row][col] == "":
        center_x, center_y = get_cell_center(row, col) # type: ignore
        
        if current_player[0] == "X":
            draw_x(board, center_x, center_y) # type: ignore
            board_state[row][col] = "X"
            current_player[0] = "O"
        else:
            draw_o(board, center_x, center_y) # type: ignore
            board_state[row][col] = "O"
            current_player[0] = "X"
        
        winner = check_winner(board_state) # type: ignore
        if winner:
            draw_text(board, f"Player {winner} wins!")
            screen.onclick(None)  # type: ignore # Disable further clicks
        elif is_board_full(board_state):
            draw_text(board, "It's a draw!")
            screen.onclick(None)  # type: ignore # Disable further clicks

def main():
    screen, board = draw_board() # type: ignore
    
    # Initialize game state
    board_state = [["" for _ in range(3)] for _ in range(3)]
    current_player = ["X"]  # Using list to make it mutable
    
    # Display initial player turn
    draw_text(board, "Player X's turn")
    
    # Set up click handling
    screen.onclick(lambda x, y: click_handler(x, y, board, board_state, current_player))
    
    # Add restart capability with 'r' key
    screen.onkey(lambda: restart_game(screen, board), "r")
    screen.listen()
    
    screen.mainloop()

def restart_game(screen, board):
    screen.clear()
    main()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
