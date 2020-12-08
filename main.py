from modules.Board import Board
from modules.Welcome import hi
import pygame as py
import sys
import time

if __name__ == '__main__':
    hi() # displays welcoming text in a console
    py.init()
    b = Board()
    # sets display resolution
    # in parentheses you may specify the % of living cells at start (20% by default)
    b.populate()
    screen = py.display.set_mode((b.height, b.width))
    b.show(screen)
    while b.alive:
        # how often should the loop be repeated in secs
        time.sleep(1)
        b.core()
        b.show(screen, (100,0,0))
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit(0)
            # to be implemented in the future:
            # elif event.type == py.KEYDOWN:
            #   if event.key == py.K_p:
            #      pause = True
            #     b.paused()
            elif event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                sys.exit(0)
            elif event.type == py.KEYDOWN and event.key == py.K_SPACE:
                print("Hello there!")
    py.display.quit()
    py.quit()
