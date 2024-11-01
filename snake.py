from tkinter import *
import random

GAME_WIDTH = 1400
GAME_HEIGHT = 1000
SPEED = 60
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "Blue"
FOOD_COLOR = "RED"
BACKGROUND_COLOR = "Black"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y, in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="Snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    global game_is_over

    x, y = snake.coordinates[0]

    if game_is_over !=1:
        if direction == 'up':
            y -= SPACE_SIZE
        elif direction == 'down':
            y += SPACE_SIZE
        elif direction == 'left':
            x -= SPACE_SIZE
        elif direction == 'right':
            x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()
    
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    window.after(SPEED, next_turn, snake, food)

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    
    if y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def change_direction(new_direction):
    global direction

    if new_direction =='left':
        if direction != 'right':
            direction = new_direction

    if new_direction =='right':
        if direction != 'left':
            direction = new_direction

    if new_direction =='up':
        if direction != 'down':
            direction = new_direction

    if new_direction =='down':
        if direction != 'up':
            direction = new_direction

def game_over():
    global game_is_over
    game_is_over = 1
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70),text="GAME OVER",fill="RED",tag="gameover")

window = Tk()
window.title("Snake")
window.resizable(False, False)

score = 0
game_is_over = 0
direction = 'down'

label = Label(text="Score: {}".format(score), font=('consolas',40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

x = int((window.winfo_screenwidth() / 2) - (GAME_WIDTH / 2))
y = int((window.winfo_screenheight() / 2 ) - (GAME_HEIGHT / 2))
window.geometry("{}x{}+{}+{}".format(GAME_WIDTH, GAME_HEIGHT, x, y))

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

window.bind('<a>', lambda event: change_direction('left'))
window.bind('<d>', lambda event: change_direction('right'))
window.bind('<w>', lambda event: change_direction('up'))
window.bind('<s>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
