from config import SPEED, canvas, window, label, SPACE_SIZE, SNAKE_COLOR, GAME_HEIGHT, GAME_WIDTH, score, game_is_over, direction, game_loop, direction_changed, BODY_PARTS, FOOD_COLOR, ALL
from class_snake import Snake
from class_food import Food

def next_turn(snake, food):
    global game_is_over, game_loop, direction_changed

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
        food = Food(snake, SPACE_SIZE, FOOD_COLOR, GAME_WIDTH, GAME_HEIGHT, canvas)
    
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        game_loop = window.after(SPEED, next_turn, snake, food)

    direction_changed = False

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
    global direction, direction_changed

    if direction_changed:
        return
    
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

    direction_changed = True

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

    snake = Snake(BODY_PARTS, SPACE_SIZE, SNAKE_COLOR, canvas)
    food = Food(snake, SPACE_SIZE, FOOD_COLOR, GAME_WIDTH, GAME_HEIGHT, canvas)

    next_turn(snake, food)