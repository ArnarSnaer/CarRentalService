# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid

def current_board(a_list): # Function will print every line of the current board setting
    for row in a_list:
        for number in row:
            print("{}".format(number), end=' ')
        print() # Used to create a new line between each row
    print()

def move_pos(current_board, given_pos, x, y):
    current_board[y][x] = EMPTY # Replace the current "o" in the board as x
    if given_pos == LEFT: # Move to the requested direction, or to the other side of the board
        if x == 0:
            x = 4
        else:
            x -= 1
    elif given_pos == RIGHT:
        if x == 4:
            x = 0
        else:
            x += 1
    elif given_pos == UP:
        if y == 0:
            y = 4
        else:
            y -= 1
    else:
        if y == 4:
            y = 0
        else:
            y += 1
    current_board[y][x] = POSITION # Rewrite the new position
    return current_board, x, y

x_axis = 0 # Default values of x and y
y_axis = 0
the_grid = initialize_grid() # First grid
while True:
    current_board(the_grid) # Prints out the board
    new_move = get_move() 
    if new_move == QUIT:
        break
    else:
        the_grid, x_axis, y_axis = move_pos(the_grid, new_move, x_axis, y_axis)