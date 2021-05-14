import random
from copy import deepcopy

import pygame

from player import Player
from maze import Maze
from items import Items


class Game:

    def __init__(self):
        # Using groups for collisions
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_walls = pygame.sprite.Group()
        self.all_items = pygame.sprite.Group()
        # Will increase when player picks an item
        self.inventory = 0
        # Items will spawn in random order
        self.item_list = ["aiguille.png", "tube_plastique.png", "seringue.png"]
        random.shuffle(self.item_list)
        # This is the layout of the maze
        # 1 = Wall, 2 = items (randomised), 3 = Guardian, 4 = Exit
        self.layout = [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1,
            1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1,
            1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1,
            1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1,
            1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1,
            1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1,
            1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
            1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1,
            1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 3, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1
        ]
        self.layout = self.place_items()
        self.draw_maze()

    def place_items(self):
        """ Randomly places items in the maze """
        item_list = 3
        layout = deepcopy(self.layout)
        while item_list:
            for index, tile in enumerate(layout):
                if tile == 0 and item_list:
                    if random.random() > 0.99:
                        layout[index] = 2
                        item_list -= 1
        return layout

    def draw_maze(self):
        # Size of the maze in height and width (both are equal)
        size = 15
        # Counters to build the maze
        column = 0
        row = 0

        # size**2 because width*height = number of tiles
        for tile in range(size**2):
            # builds a wall and rect each time it encounters 1
            if self.layout[row + column * size] == 1:
                # We create an instance of Maze and add it to wall group
                wall = Maze(self, row*32, column*32)
                self.all_walls.add(wall)

            # 2 = Items, randomised with self.place_items()
            elif self.layout[row + column * size] == 2:
                asset_name = self.item_list.pop()
                item = Items(self, asset_name, row*32, column*32)
                self.all_items.add(item)

            column += 1
            if column > size - 1:
                column = 0
                row += 1

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(
            sprite, group, False, pygame.sprite.collide_mask)
