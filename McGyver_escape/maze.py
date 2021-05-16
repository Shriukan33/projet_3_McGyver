import pygame

from pathlib import Path

# Set this constant to make it simple to point to ressources folder
ASSETS = str(Path(__file__).resolve().parent) + "/ressources/"


class Maze(pygame.sprite.Sprite):
    """Handles skin of walls"""

    def __init__(self, game, x_pos, y_pos):
        # We call the init of parent class Sprite
        super().__init__()
        # We set a Game instance to check for collisions
        self.game = game
        # We load and resize the wall skin to 32x32
        self.image = pygame.image.load(ASSETS + "wall.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        # When we create a wall, we give the coordinates with x_pos and y_pos
        self.rect.x = x_pos
        self.rect.y = y_pos
