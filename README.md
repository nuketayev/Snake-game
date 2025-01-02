# Snake Game

This is a Snake game implemented in Python using the Tkinter library. The game involves controlling a snake to eat food and grow in size while avoiding collisions with the walls or itself.

## Purpose and Features

The purpose of this project is to provide an implementation of the classic Snake game. The main features of the game include:
- Controlling the snake using arrow keys or WASD keys
- Growing the snake's size when it eats food
- Increasing the game speed as the score increases
- Displaying the current score
- Restarting the game when the snake collides with the walls or itself

## Running the Game

### Dependencies

The game requires Python and the Tkinter library. Tkinter is included with most Python installations. If you don't have Tkinter, you can install it using the following command:

```bash
pip install tk
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/nuketayev/Snake-game.git
```

2. Navigate to the project directory:
```bash
cd Snake-game
```

3. Run the game:
```bash
python game.py
```

## Code Structure

The project consists of the following main files:

- `game.py`: The main file that initializes the game and handles user input.
- `class_snake.py`: Contains the `Snake` class, which represents the snake in the game.
- `class_food.py`: Contains the `Food` class, which represents the food in the game.
- `game_functions.py`: Contains various functions for handling game logic, such as moving the snake, checking for collisions, and restarting the game.
- `config.py`: Contains configuration variables for the game, such as the game window size, snake color, and speed.

## Contributing

If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository and create a new branch for your feature or bugfix.
2. Make your changes and ensure that the code is properly formatted and documented.
3. Submit a pull request with a clear description of your changes and the problem they solve.

Thank you for your contributions!
