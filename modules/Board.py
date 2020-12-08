from random import randrange
import pygame as py
import numpy as np


class Board:

    def __init__(self, height=500, width=500):
        # setting resolution
        py.display.set_caption('Gra w życie')
        self.height = height
        self.width = width
        self.board_area = height * width
        # setting rules
        self.death = (0, 1, 4, 5, 6, 7, 8)
        self.survives = 3
        # to be implemented in the future
        """self.tps = 10
        self.tps_clock = py.time.Clock()
        self.tps_delta = 0.0"""
        self.alive = set()
        super().__init__()

    def show(self, window, living_col=(120,252,0), dead_col=(0,0,0)):
        py.draw.rect(window, living_col, py.Rect(0, 0, self.width, self.height))
        for cell_coordinates in self.alive:
            # please note that one cell has a height and width on one pixel
            py.draw.rect(window, dead_col, py.Rect((cell_coordinates), (1, 1)))
        py.display.update()

    def populate(self):
        volumestr = input("How many % of the board should be populated? ")
        if volumestr.startswith('-'):
            print("Invalid input, 20% of the board will be populated.")
            volumestr = '20'
        try:
            volumefloat = float(volumestr)/100
            print(f'{int(volumestr)}% of the board will be populated.')
        except ValueError:
            print("Invalid input, 20% of the board will be populated.")
            volumefloat = 0.2
        all_population = self.board_area * volumefloat
        while len(self.alive) < all_population:
            # randomly choose a place for the cell
            cell = (randrange(self.height), randrange(self.width))
            # add a cell to the set storing information about living cells
            self.alive.add(cell)

    def neigh(self, cell):
        x, y = cell
        # Checks all neighbours of the cell
        # True gives 1, False gives 0
        return (((x+1, y) in self.alive) + ((x+1, y+1) in self.alive) +
                ((x+1, y-1) in self.alive) + ((x-1,y) in self.alive) +
                ((x-1, y+1) in self.alive) + ((x-1, y-1) in self.alive) +
                ((x, y+1) in self.alive) + ((x, y-1) in self.alive))

    def core(self):
        # copy the previous state
        reload = self.alive.copy()
        for cell in self.alive:
            counter = self.neigh(cell)
            if counter in self.death:
                reload.remove(cell)
            x, y = cell
            if self.neigh((x+1, y)) == self.survives:
                reload.add((x+1, y))
            if self.neigh((x+1, y+1)) == self.survives:
                reload.add((x+1,y+1))
            if self.neigh((x+1,y-1)) == self.survives:
                reload.add((x+1, y-1))
            if self.neigh((x-1,y)) == self.survives:
                reload.add((x-1,y))
            if self.neigh((x-1, y+1)) == self.survives:
                reload.add((x-1,y+1))
            if self.neigh((x-1, y-1)) == self.survives:
                reload.add((x-1,y-1))
            if self.neigh((x,y+1)) == self.survives:
                reload.add((x,y+1))
            if self.neigh((x, y-1)) == self.survives:
                reload.add((x,y-1))
        # updates the old set of living cells.
        self.alive = reload
