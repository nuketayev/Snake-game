from tkinter import *
from class_snake import Snake
from class_food import Food
from game_functions import next_turn, restart, change_direction
from config import window, canvas, label, restart_button, SPACE_SIZE, GAME_WIDTH, GAME_HEIGHT, BODY_PARTS, SNAKE_COLOR, FOOD_COLOR

restart_button.config(command=restart)

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

window.bind('<a>', lambda event: change_direction('left'))
window.bind('<d>', lambda event: change_direction('right'))
window.bind('<w>', lambda event: change_direction('up'))
window.bind('<s>', lambda event: change_direction('down'))

snake = Snake(BODY_PARTS, SPACE_SIZE, SNAKE_COLOR, canvas)
food = Food(snake, SPACE_SIZE, FOOD_COLOR, GAME_WIDTH, GAME_HEIGHT, canvas)

next_turn(snake, food)

window.mainloop()