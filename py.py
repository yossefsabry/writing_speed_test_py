# import methods and library's ->
# -------------------------------------------------
import curses
from curses import wrapper
import time
import random


# from curses.textpad import Textbox, rectangle
# import time


# screen and for welcome and start typing
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(" welcome in  the speed typing test! ")
    stdscr.addstr("\n press any key to begin!")
    stdscr.addstr(6, 0, "# enter Esc to close the program #")
    stdscr.refresh()
    stdscr.getkey()


def display_test(stdscr, target, current, wpm=0, time_elapsed=0):
    stdscr.addstr(target)
    stdscr.addstr(4, 0, f"- WPM : {wpm}")
    stdscr.addstr(5, 0, f"- time :  {time_elapsed:.2f} second")

    # Calculate accuracy
    accuracy = 0
    if len(target) > 0:
        accuracy = (sum(1 for a, b in zip(target, current) if a == b) / len(target)) * 100

    stdscr.addstr(6, 0, f"- Accuracy: {accuracy:.2f}%")

    # make enumerate to check the element index to use for check if  true of false
    for i, char in enumerate(current):
        # if the char is true color gone be green
        correct_char = target[i]
        color = curses.color_pair(1)
        # if false the color gone be red
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)


# make def for load the text from the file text.txt
def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


# start test for typing
def wpm_test(stdscr):
    target_text = load_text()
    current_test = []
    wpm = 0
    start_time = time.time()
    # no delay for new wait form user input to calc the wpm
    stdscr.nodelay(True)

    stdscr.clear()
    stdscr.addstr(target_text, curses.A_BOLD)
    stdscr.refresh()

    while True:

        # every time calc the time
        time_elapsed = max(time.time() - start_time, 1)
        # the equation for wpm
        wpm = round((len(current_test) / (time_elapsed / 60)) / 5)
        stdscr.clear()
        # the line under time_elapsed beceuse change to int not float
        display_test(stdscr, target_text, current_test, wpm, time_elapsed)
        stdscr.refresh()

        # the main idea after make wpm  to handle the error and continue
        # if "".join(current_test) == target_text:
        if "".join(current_test) == target_text or len(current_test) == len(target_text):
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        # every key in the keyboard present something and escape "Esc" key present 27
        # so every time I click on the button its gone to break the loop
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_test) > 0:
                current_test.pop()

        elif len(current_test) < len(target_text):
            current_test.append(key)


# the main function for call all the other function
def main(stdscr):
    # making color ->
    # ----------------------------------------------
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    # shortcuts for color

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, " you completed the text press any key to continue ....")
        key = stdscr.getkey()
        # if user input Esc key its will break
        if ord(key) == 27:
            break


wrapper(main)
