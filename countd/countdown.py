"""Countdown, by Al Sweigart al@inventwithpython.com
Show a countdown timer animation using a seven-segment display.
Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
This code is available at
https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic"""

import sys
import time
import sevseg  # Imports our sevseg.py program.

# (!) Change this to any number of seconds:
SECONDS_LEFT = 30

try:
    while True:  # Main program loop.
        # Clear the screen by printing several newlines:
        print('\n' * 60)

        # Get the hours/minutes/seconds from secondsLeft:
        # For example: 7265 is 2 hours, 1 minute, 5 seconds.
        # So 7265 // 3600 is 2 hours:
        HOURS = str(SECONDS_LEFT // 3600)
        # And 7265 % 3600 is 65, and 65 // 60 is 1 minute:
        MINUTES = str((SECONDS_LEFT % 3600) // 60)
        # And 7265 % 60 is 5 seconds:
        SECONDS = str(SECONDS_LEFT % 60)

        # Get the digit strings from the sevseg module:
        H_DIGITS = sevseg.get_sevseg_str(HOURS, 2)
        hTopRow, hMiddleRow, hBottomRow = H_DIGITS.splitlines()

        M_DIGITS = sevseg.get_sevseg_str(MINUTES, 2)
        mTopRow, mMiddleRow, mBottomRow = M_DIGITS.splitlines()

        S_DIGITS = sevseg.get_sevseg_str(SECONDS, 2)
        sTopRow, sMiddleRow, sBottomRow = S_DIGITS.splitlines()

        # Display the digits:
        print(hTopRow + '     ' + mTopRow + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        if SECONDS_LEFT == 0:
            print()
            print('    * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)  # Insert a one-second pause.
        SECONDS_LEFT -= 1
except KeyboardInterrupt:
    print('Countdown, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # When Ctrl-C is pressed, end the program.)
