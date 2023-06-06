import time
import random
import colorama
import curses

try:
    # Initialize curses screen
    stdscr = curses.initscr()

    # Create cube vertices
    vertices = [
        (-1,-1,-1), (-1,-1,1), (-1,1,-1),
        (-1,1,1), (1,-1,-1), (1,-1,1),
        (1,1,-1), (1,1,1)
    ]

    # Define edges between vertices
    edges = [
        (0, 1), (0, 2), (0, 4), (1, 3),
        (1, 5), (2, 3), (2, 6), (3, 7),
        (4, 5), (4, 6), (5, 7), (6, 7)
    ]

    # Define cursor position and ASCII character for drawing
    x, y, z = 0, 0, 0
    char = "#"

    # Loop through all edges and draw them as lines on screen
    for edge in edges:
        start = vertices[edge[0]]
        end = vertices[edge[1]]
        stdscr.addstr(int(start[1])+y, int(start[0])+x, char)
        stdscr.addstr(int(end[1])+y, int(end[0])+x, char)

    # Refresh the screen and wait for user input
    stdscr.refresh()
    stdscr.getch()

finally:
    # End the curses session
    curses.endwin()
