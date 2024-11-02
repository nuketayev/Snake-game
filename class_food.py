import random

class Food:
    def __init__(self, snake, SPACE_SIZE, FOOD_COLOR, GAME_WIDTH, GAME_HEIGHT, canvas):
        while True:
            x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
            y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
            self.coordinates = [x,y]

            if self.coordinates not in snake.coordinates:
                break

        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="food")