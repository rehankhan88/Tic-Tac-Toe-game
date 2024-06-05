
from ursina import *

app = Ursina()

# Initialize the player entity with name 'O' and a specific color
player = Entity(name='O', color=color.rgb(178, 102, 255))

# Create a tooltip (cursor) that displays the current player's name and color
Cursor = Tooltip(player.name, color=player.color, origin=(0,0), scale=2, enabled=True)
Cursor.background.color = color.clear

# Hide the default mouse cursor
mouse.visibility = False

# Create a 3x3 board to hold the buttons (tic-tac-toe grid)
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

# Function to check if there is a winner
def check_winner():
    name = player.name
    
    # Check all possible winning combinations
    won = (
        (board[0][0].text == name and board[0][1].text == name and board[0][2].text == name) or  # horizontal top
        (board[1][0].text == name and board[1][1].text == name and board[1][2].text == name) or  # horizontal middle
        (board[2][0].text == name and board[2][1].text == name and board[2][2].text == name) or  # horizontal bottom
        
        (board[0][0].text == name and board[1][0].text == name and board[2][0].text == name) or  # vertical left
        (board[0][1].text == name and board[1][1].text == name and board[2][1].text == name) or  # vertical middle
        (board[0][2].text == name and board[1][2].text == name and board[2][2].text == name) or  # vertical right
        
        (board[0][0].text == name and board[1][1].text == name and board[2][2].text == name) or  # diagonal \
        (board[2][0].text == name and board[1][1].text == name and board[0][2].text == name)     # diagonal /
    )
    
    if won:
        print("Winner is:", name)

# Create the grid of buttons
for x in range(3):
    for y in range(3):
        b = Button(parent=scene, position=(x, y))
        board[x][y] = b
        
        # Define what happens when a button is clicked
        def on_click(b=b):
            b.text = player.name
            b.color = player.color
            b.collision = False  # Disable further clicks on this button
            check_winner()  # Check if this move wins the game
            
            # Switch player
            if player.name == 'O':
                player.name = 'X'
                player.color = color.rgb(204, 255, 153)
            else:
                player.name = 'O'
                player.color = color.rgb(178, 102, 255)
                
            # Update the cursor to show the next player's name and color
            Cursor.text = player.name
            Cursor.color = player.color

        b.on_click = on_click  # Assign the on_click function to the button

app.run()
