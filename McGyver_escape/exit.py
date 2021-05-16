from pathlib import Path

import pygame

# Set this constant to make it simple to point to ressources folder
ASSETS = str(Path(__file__).resolve().parent) + "/ressources/"


class Exit(pygame.sprite.Sprite):
    """Handles collision with player and appearance of exits"""

    def __init__(self, game, x_pos, y_pos):
        super().__init__()
        self.game = game
        self.image = pygame.image.load(ASSETS + "exit.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def check_exit(self):
        """Checks player collision with exit, and enables win screen"""

        if self.game.check_collision(self, self.game.all_players):
            self.game.main_game = False
            self.game.win_screen = True
