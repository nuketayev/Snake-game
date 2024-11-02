from tkinter import *
import random

NUM_BOXES_WIDTH = 30
NUM_BOXES_HEIGHT = 20
SPACE_SIZE = 50
GAME_WIDTH = NUM_BOXES_WIDTH * SPACE_SIZE
GAME_HEIGHT = NUM_BOXES_HEIGHT * SPACE_SIZE

SPEED = 100

BODY_PARTS = 3
SNAKE_COLOR = "Blue"
FOOD_COLOR = "RED"
BACKGROUND_COLOR = "black"


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
    def __init__(self, snake):
        while True:
            x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
            y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
            self.coordinates = [x,y]

            if self.coordinates not in snake.coordinates:
                break

        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    global game_is_over, game_loop

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
        global SPEED
        if (score % 5) == 0 and SPEED !=40:
            SPEED -= 20
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food(snake)
    
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        game_loop = window.after(SPEED, next_turn, snake, food)

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

def restart():
    global snake, food, score, direction, game_is_over, SPEED
    window.after_cancel(game_loop)
    canvas.delete(ALL)

    score = 0
    direction = 'down'
    game_is_over = 0
    SPEED = 100

    label.config(text="Score: {}".format(score))

    snake = Snake()
    food = Food(snake)

    next_turn(snake, food)


window = Tk()
window.title("Snake")
window.config(bg="#282828")
window.resizable(False, False)

score = 0
game_is_over = 0
direction = 'down'
game_loop = None


canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack(side="bottom")

label = Label(window, text="Score: {}".format(score), font=('consolas', 45), bg="#282828", fg="Gold")
label.pack(side="left")

restart_button = Button(window, text="Restart", command=restart, bg="black", fg="white")
restart_button.pack(side="right")




window.update()

x = int((window.winfo_screenwidth() / 2) - (GAME_WIDTH / 2))
y = int((window.winfo_screenheight() / 2 ) - ((GAME_HEIGHT+100) / 2))
window.geometry("{}x{}+{}+{}".format(GAME_WIDTH, GAME_HEIGHT+100, x, y))

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

window.bind('<a>', lambda event: change_direction('left'))
window.bind('<d>', lambda event: change_direction('right'))
window.bind('<w>', lambda event: change_direction('up'))
window.bind('<s>', lambda event: change_direction('down'))

snake = Snake()
food = Food(snake)

next_turn(snake, food)

window.mainloop()
