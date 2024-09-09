# Flower Drawing Program

## Overview

This Python program uses the Turtle graphics library to draw flowers based on user input. You can choose from different types of flowers and specify how many petals each flower should have. The program also supports plural forms of flower names.

## Features

- Draws different types of flowers (Sunflower, Rose, Lily, Lotus, Tulip).
- Allows you to specify the number of petals and flowers.
- Handles plural forms of flower names (e.g., "roses").

## How to Use

1. **Run the Program**: Execute the script to start the program.

2. **Input**: When prompted, enter the number of flowers, the type of flower, and optionally use plural forms. For example:
   - `4 roses`
   - `3 sunflowers`

3. **Viewing the Drawing**: The Turtle graphics window will open and display the flowers based on your input. The window will remain open until you close it.

## Code Breakdown

### `Flower` Class

- **Attributes**:
  - `spacer`: Keeps track of the position for drawing each flower.
  - `num_petals`: Number of petals for each flower.
  - `num_flowers`: Number of flowers to draw.
  - `type_of_flower`: Type of flower to draw.
  - `spacing`: Space between flowers.

- **Methods**:
  - `__init__`: Initializes the flower drawing setup.
  - `speed`: Sets the drawing speed.
  - `draw_flower1`: Draws the specified number of flowers in a row.
  - `draw_flower`: Draws a single flower with petals and a stem.
  - `done_drawing`: Keeps the Turtle graphics window open.

### `main` Function

- Calls the `prompt` function to get user input and then creates a `Flower` object to draw the flowers.

### `prompt` Function

- Prompts the user for input and extracts the number of flowers and type of flower from the input.
- Handles both singular and plural flower names.

### `itemMatching` Function

- Matches the flower type from the user input to the available flower types.
- Supports both singular and plural flower names.

### `numberSelector` Function

- Selects the number closest to the flower type based on its position in the input string.

### `verifyNum` Function

- Ensures that the input is a valid number.

### `guidelines` Function

- Handles cases where the input does not match any expected values.

## Requirements

- Python 3.x
- Turtle graphics library (usually included with Python installations)

## How to Run

1. Make sure you have Python installed on your computer.
2. Save the script as `flower_drawing.py`.
3. Open a terminal or command prompt and navigate to the directory where the script is saved.
4. Run the script using the command: `python flower_drawing.py`.

## Troubleshooting

- **Program Doesn't Run**: Ensure you have Python and the Turtle library installed.
- **Input Not Recognized**: Make sure to enter the input correctly (e.g., "4 roses").

## License

This program is free to use and modify. Enjoy creating beautiful flower drawings!
