"""Sevseg, by Al Sweigart al@inventwithpython.com
A seven-segment number display module, used by the Countdown and Digital
Clock programs.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
This code is available at
https://nostarch.com/big-book-small-python-programming
Tags: short, module

A labeled seven-segment display, with each segment labeled A to G:
 __A__
|     |    Each digit in a seven-segment display:
F     B     __       __   __        __   __  __   __   __
|__G__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
|     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
E     C
|__D__|"""


def get_sevseg_str(number, min_width=0):
    """Return a seven-segment display string of number. The returned
    string will be padded with zeros if it is smaller than minWidth."""

    # Convert number to string in case it's an int or float:
    number = str(number).zfill(min_width)

    # Define patterns for each character
    digit_patterns = {
        '.': (' ', ' ', '.'),
        '-': ('    ', ' __ ', '    '),
        '0': (' __ ', '|  |', '|__|'),
        '1': ('    ', '   |', '   |'),
        '2': (' __ ', ' __|', '|__ '),
        '3': (' __ ', ' __|', ' __|'),
        '4': ('    ', '|__|', '   |'),
        '5': (' __ ', '|__ ', ' __|'),
        '6': (' __ ', '|__ ', '|__|'),
        '7': (' __ ', '   |', '   |'),
        '8': (' __ ', '|__|', '|__|'),
        '9': (' __ ', '|__|', ' __|')
    }

    # Initialize the rows for display
    rows = ['', '', '']

    for i, numeral in enumerate(number):
        # Get the pattern for the numeral from the dictionary
        pattern = digit_patterns.get(numeral, ('   ', '   ', '   '))
        rows[0] += pattern[0]
        rows[1] += pattern[1]
        rows[2] += pattern[2]

        # Add space between digits except for decimal points
        if i != len(number) - 1 and number[i + 1] != '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)


# If this program isn't being imported, display the numbers 00 to 99
if __name__ == '__main__':
    print('This module is meant to be imported rather than run.')
    print('For example, this code:')
    print('    import sevseg')
    print('    myNumber = sevseg.getSevSegStr(42, 3)')
    print('    print(myNumber)')
    print()
    print('...will print 42, zero-padded to three digits:')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')
