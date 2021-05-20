import random
from copy import deepcopy

import pygame

from player import Player, ASSETS
from maze import Maze
from items import Items
from guard import Guard
from exit import Exit


class Game:
    """Handles sprite groups, maze building, inventory and collision checks"""

    def __init__(self):

        # Bools to access different screens
        self.main_game = True
        self.lose_screen = False
        self.win_screen = False
        # Using groups for collisions
        self.all_players = pygame.sprite.Group()
        self.all_guards = pygame.sprite.Group()
        self.all_walls = pygame.sprite.Group()
        self.all_exits = pygame.sprite.Group()
        self.all_items = pygame.sprite.Group()
        # Will increase when player picks an item
        self.inventory = 0
        # Items will spawn in random order
        self.item_list = ["aiguille.png", "tube_plastique.png", "ether.png"]
        random.shuffle(self.item_list)
        # This is the layout of the maze
        # 1 = Wall, 2 = items (randomised), 3 = Guardian, 4 = Exit, 5 = Player
        self.layout = [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 5, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
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
        """ Randomly places items in the maze

        It searches for 0 (=free space) in the self.layout, and apply a chance
        place an item on said position.
        """

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
        """Draws the self.layout's content on screen and creates different entities

        Each number in self.layout corresponds to an element of the maze.
        0 = Free space to walk and place items
        1 = Walls blocking the player
        2 = items placed by the place_items function at random
        3 = Guard : kills the player if he doesn't have all 3 items
        4 = Exit : Enables the win screen
        5 = Start position of player
        At each number (except 0) a sprite is created and added to its group
        """

        # Size of the maze in height and width (both are equal)
        size = 15
        # Counters to build the maze
        column = 0
        row = 0

        # size**2 because width*height = number of tiles
        for tile in range(size**2):
            # 1 = walls
            if self.layout[row + column * size] == 1:
                # We create an instance of Maze and add it to wall group
                wall = Maze(self, row*32, column*32)
                self.all_walls.add(wall)

            # 2 = Items, randomised with self.place_items()
            elif self.layout[row + column * size] == 2:
                asset_name = self.item_list.pop()
                item = Items(self, asset_name, row*32, column*32)
                self.all_items.add(item)

            # 3 = Guard
            elif self.layout[row + column * size] == 3:
                guard = Guard(self, row*32, column*32)
                self.all_guards.add(guard)

            # 4 = Exit
            elif self.layout[row + column * size] == 4:
                exit = Exit(self, row*32, column*32)
                self.all_exits.add(exit)

            # 5 = Player
            elif self.layout[row + column * size] == 5:
                self.player = Player(self, row*32, column*32)
                self.all_players.add(self.player)

                # Entrance addead beneath player
                entrance = Maze(self, row*32, column*32)
                entrance.image = pygame.image.load(ASSETS + "entrance.png")
                entrance.image = pygame.transform.scale(
                    entrance.image, (32, 32))
                self.all_walls.add(entrance)

            column += 1
            if column > size - 1:
                column = 0
                row += 1

    def check_collision(self, sprite, group):
        """Checks for collision between a sprite and a group of sprites"""

        return pygame.sprite.spritecollide(
            sprite, group, False, pygame.sprite.collide_mask)
