from tkinter import Tk, Canvas, Label, Button

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

window = Tk()
window.title("Snake")
window.config(bg="#282828")
window.resizable(False, False)

score = 0
game_is_over = 0
direction = 'down'
game_loop = None
direction_changed = False

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack(side="bottom")

label = Label(window, text="Score: {}".format(score), font=('consolas', 45), bg="#282828", fg="Gold")
label.pack(side="left")

restart_button = Button(window, text="Restart", font=('Arial', 50), bg="black", fg="white")
restart_button.pack(side="right")

window.update()

x = int((window.winfo_screenwidth() / 2) - (GAME_WIDTH / 2))
y = int((window.winfo_screenheight() / 2 ) - ((GAME_HEIGHT+100) / 2))
window.geometry("{}x{}+{}+{}".format(GAME_WIDTH, GAME_HEIGHT+100, x, y))

ALL = "all"