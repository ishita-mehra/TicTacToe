import tkinter as tk
from tkinter import messagebox

# Initialize the game
game = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

# Function to handle button click
def button_click(row, col):
    global current_player

    # Check if the clicked cell is already occupied
    if game[row][col] != ' ':
        return

    # Update the game board
    game[row][col] = current_player
    buttons[row][col].config(text=current_player)

    # Check for a win or a tie
    if check_win(current_player):
        messagebox.showinfo('Game Over', f'Player {current_player} wins!')
        reset_game()
    elif check_tie():
        messagebox.showinfo('Game Over', 'It\'s a tie!')
        reset_game()
    else:
        # Switch to the other player's turn
        current_player = 'O' if current_player == 'X' else 'X'

# Function to check for a win
def check_win(player):
    # Check rows
    for row in range(3):
        if game[row][0] == game[row][1] == game[row][2] == player:
            return True
    # Check columns
    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col] == player:
            return True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] == player:
        return True
    if game[0][2] == game[1][1] == game[2][0] == player:
        return True
    return False

# Function to check for a tie
def check_tie():
    for row in range(3):
        for col in range(3):
            if game[row][col] == ' ':
                return False
    return True

# Function to reset the game
def reset_game():
    global game, current_player
    game = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ', state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title('Tic Tac Toe')

# Create buttons
buttons = [[None, None, None] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(window, text=' ', font=('Arial', 20), width=5, height=2,
                                     command=lambda r=row, c=col: button_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Start the main loop
window.mainloop()
