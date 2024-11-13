# Seven Segment Countdown Display

This project provides a seven-segment display module for creating digital-style numeric displays, commonly seen in countdown timers, digital clocks, and other visual numerical displays.

## Overview

The main file, `sevseg.py`, includes a function that converts numbers into a seven-segment display format. Additionally, `countdown.py` uses this function to create a countdown timer that displays numbers in a seven-segment style.

### Features

- **Seven-Segment Display Module**: Converts any integer or float into a seven-segment display format.
- **Countdown Timer**: Uses the seven-segment display to create a visually appealing countdown.
- **Easy Customization**: The display function accepts padding and formatting options, making it adaptable to various use cases.

## Installation

No additional libraries are required. Simply clone or download the repository and run the Python files.

```bash
git clone https://github.com/yourusername/seven-segment-countdown.git
cd seven-segment-countdown
```

## Usage

1. **Seven-Segment Display Module**  
   You can use `sevseg.py` independently to convert any number to a seven-segment string.

   ```python
   import sevseg

   number_str = sevseg.get_sevseg_str(42, 3)
   print(number_str)
   ```

2. **Countdown Timer**  
   Run `countdown.py` to see the countdown timer in action:

   ```bash
   python countdown.py
   ```

## Code Structure

- `sevseg.py`: Contains the `get_sevseg_str()` function, which creates a seven-segment representation for a number.
- `countdown.py`: A script that implements a countdown timer using `sevseg.py` to format and display each second.

## Example Output

Here's an example output for displaying the number "42" in a seven-segment style with padding:

```
 __      __ 
|  |   |__| 
|__|      | 
```

## License

This project is open-source and available under the MIT License.

