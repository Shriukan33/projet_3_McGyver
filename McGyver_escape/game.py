import pygame

from player import Player
from maze import Maze


class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_walls = pygame.sprite.Group()
        # pressed will contain all key pressed at the each frame
        self.pressed = {}
        # This is the layout of the maze
        # 1 = Wall, 2 = Player, 3 = Guardian, 4 = Exit
        self.layout = [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
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
        self.draw_maze()

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

            column += 1
            if column > size - 1:
                column = 0
                row += 1

    def check_collision(self, sprite, group):
        print(pygame.sprite.spritecollide(
            sprite, group, False, pygame.sprite.collide_mask))
        return pygame.sprite.spritecollide(
            sprite, group, False, pygame.sprite.collide_mask)
