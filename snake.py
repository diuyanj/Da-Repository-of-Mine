import tkinter as tk
import random

ROWS = 25
COLM = 25
TILE_SIZE = 25

WIDTH = TILE_SIZE * ROWS
HEIGHT = TILE_SIZE * COLM

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# game window
app = tk.Tk()
app.title("Snake game")
app.resizable(False, False)

canvas = tk.Canvas(app, bg = 'black', width= WIDTH, height= HEIGHT, borderwidth= 0, highlightthickness= 0)
canvas.pack()
app.update()

# centering the window
app_width = app.winfo_width()
app_height = app.winfo_height()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

app_location_x = int(screen_width/2 - app_width/2)
app_location_y = int(screen_height/2 - app_height/2)

app.geometry(f'{app_width}x{app_height}+{app_location_x}+{app_location_y}')


# game initialization
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE)
food = Tile(10*TILE_SIZE, 5*TILE_SIZE)
snake_body = []
append_body = []

# movement direction
velocity_x = 0
velocity_y = 0
moving = 0

def wait_for_move():
    global moving
    moving = 1

def handle_keypress(e):
    global velocity_x, velocity_y

    if not moving:
        if e.keysym == 'Up' and velocity_y != 1:
            # y - 1
            velocity_x = 0
            velocity_y = -1
            wait_for_move()
        if e.keysym == 'Down' and velocity_y != -1:
            # y + 1
            velocity_x = 0
            velocity_y = 1
            wait_for_move()
        if e.keysym == 'Left' and velocity_x != 1:
            # x - 1
            velocity_x = -1
            velocity_y = 0
            wait_for_move()
        if e.keysym == 'Right' and velocity_x != -1:
            # x + 1
            velocity_x = 1
            velocity_y = 0
            wait_for_move()    

def handle_keyrelease(e):
    pass

def move():
    global snake
    
    for i in range(len(snake_body)-1,-1,-1):
        print(i)
        tile = snake_body[i]
        if i == 0:
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y



    # Grow snake
    if snake.x == food.x and snake.y == food.y:
        # print("Nom nom nom")
        append_body.append(Tile(food.x, food.y))
        # Need to update to not spawn ontop of snake
        food.x = random.randrange(0,COLM - 1) * TILE_SIZE
        food.y = random.randrange(0,ROWS - 1) * TILE_SIZE

    if append_body:
        if append_body[0] in snake_body:
            print("TEST")
        else:
            snake_body.append(append_body.pop())
            
    snake.x += velocity_x * TILE_SIZE
    snake.y += velocity_y * TILE_SIZE    
    
    if snake.x >= app_width:
        snake.x = 0
    elif snake.x < 0:
        snake.x = app_width - TILE_SIZE
    if snake.y < 0:
        snake.y = app_height - TILE_SIZE
    elif snake.y >= app_height:
        snake.y = 0


def draw():
    global snake, moving
    move()
    canvas.delete('all')

    # Draw food
    canvas.create_rectangle(food.x, food.y,
                            food.x + TILE_SIZE,
                            food.y + TILE_SIZE,
                            fill= 'red')

    #Draw snake
    canvas.create_rectangle(snake.x, snake.y,
                            snake.x+TILE_SIZE,
                            snake.y + TILE_SIZE,
                            fill = 'lime green')
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y,
                            tile.x + TILE_SIZE,
                            tile.y + TILE_SIZE,
                            fill= 'lime green')



    app.after(500, draw)
    moving = 0

draw()

app.bind('<KeyPress>', handle_keypress)
app.bind('<KeyRelease>', handle_keyrelease)
app.mainloop()